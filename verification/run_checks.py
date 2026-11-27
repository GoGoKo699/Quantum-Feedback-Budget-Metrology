"""Finite checks for the monitored feedback-budget protocols."""

import cmath
import itertools
import math
import random
import statistics


def integrate(function, upper, panels=4096):
    step = upper / panels
    middle = math.fsum((4 if index % 2 else 2) * function(index * step)
                       for index in range(1, panels))
    return step * (function(0) + middle + function(upper)) / 3


def telegraph_moments(duration, rate):
    mean = -math.expm1(-2 * rate * duration) / (2 * rate)
    return mean, (duration - mean) / rate


def albarelli_information(count, kappa, duration):
    transient = math.exp(-kappa * duration)
    return (count**2 * (1 - transient)**2
            + count * (2 * kappa * duration + 1 - (2 - transient)**2)) / kappa**2


def stopped_information(count, rate, duration, budget, panels=4096):
    def second_after_stop(stop):
        mean, second = telegraph_moments(duration - stop, rate)
        protected = count * stop
        return (protected**2 + 2 * protected * count * mean
                + count * second + count * (count - 1) * mean**2)

    if budget == 0:
        return second_after_stop(0)

    total_rate = count * rate
    scaled_duration = total_rate * duration
    no_stop = math.fsum(math.exp(-scaled_duration + index * math.log(scaled_duration)
                                 - math.lgamma(index + 1))
                         for index in range(budget))

    def integrand(stop):
        if stop == 0:
            return total_rate * second_after_stop(0) if budget == 1 else 0
        scaled_stop = total_rate * stop
        density = total_rate * math.exp((budget - 1) * math.log(scaled_stop)
                                        - scaled_stop - math.lgamma(budget))
        return density * second_after_stop(stop)

    return (count * duration)**2 * no_stop + integrate(integrand, duration, panels)


def sample_records(generator, rates, duration):
    events = []
    for sensor, rate in enumerate(rates):
        time = generator.expovariate(rate)
        while time < duration:
            events.append((time, sensor))
            time += generator.expovariate(rate)
    return sorted(events)


def apply_policy(records, duration, windows, weights, budget, delay=0):
    toggles = records.copy()
    corrections = 0
    for time, sensor in records:
        if corrections < budget and time < windows[sensor] and time + delay < duration:
            toggles.append((time + delay, sensor))
            corrections += 1
    previous = [0.0] * len(weights)
    times = [0.0] * len(weights)
    signs = [1] * len(weights)
    for time, sensor in sorted(toggles):
        times[sensor] += signs[sensor] * (time - previous[sensor])
        previous[sensor] = time
        signs[sensor] *= -1
    exposure = math.fsum(weight * (subtotal + sign * (duration - time))
                         for weight, subtotal, sign, time in
                         zip(weights, times, signs, previous))
    return exposure, signs, corrections


def average_and_error(samples):
    return statistics.fmean(samples), statistics.stdev(samples) / math.sqrt(len(samples))


def check_telegraph_and_stopping():
    for rate, duration in itertools.product((0.3, 1.0, 1.7), (0.2, 1, 10)):
        mean, second = telegraph_moments(duration, rate)
        assert math.isclose(mean, integrate(lambda time: math.exp(-2 * rate * time),
                                            duration), rel_tol=2e-10)
        assert math.isclose(second, integrate(
            lambda time: 2 * (duration - time) * math.exp(-2 * rate * time), duration),
            rel_tol=2e-10)
        for count in (1, 2, 4, 11):
            expected = albarelli_information(count, 2 * rate, duration)
            actual = stopped_information(count, rate, duration, 0)
            assert math.isclose(actual, expected, rel_tol=1e-11)

    count, rate, duration = 4, 1.0, 10
    generator = random.Random(20261127)
    samples = {0: [], 20: [], 40: []}
    for _ in range(30_000):
        records = sample_records(generator, (rate,) * count, duration)
        for budget, results in samples.items():
            value, _, corrections = apply_policy(records, duration, (duration,) * count,
                                                 (1,) * count, budget)
            assert corrections == min(budget, len(records))
            results.append(value**2)

    for budget, reference in ((0, 40.999999992), (20, 520.788002500), (40, 1474.492044070)):
        calculated = stopped_information(count, rate, duration, budget)
        refined = stopped_information(count, rate, duration, budget, panels=8192)
        observed, error = average_and_error(samples[budget])
        assert math.isclose(calculated, refined, rel_tol=1e-9)
        assert math.isclose(refined, reference, rel_tol=1e-10)
        assert abs(observed - refined) < 5 * error
        print(f"Cap {budget:2d}: F={refined:.6f}; simulation {observed:.4f} ± {error:.4f} SE")


def rotate_signal(state, weights, frequency, duration):
    for basis, amplitude in enumerate(state):
        weight = math.fsum((-weight if basis & (1 << sensor) else weight)
                           for sensor, weight in enumerate(weights))
        state[basis] = amplitude * cmath.exp(-0.5j * frequency * duration * weight)


def check_ghz_parity():
    weights = (0.8, 1.1, 1.7)
    records = [(0.1, 1), (0.4, 0), (0.6, 0), (1.1, 1), (1.2, 0), (1.6, 2)]
    duration = 1.7
    for budget, frequency in itertools.product((0, 2, 6), (-0.32, 0, 0.18)):
        state = [0j] * 8
        state[0] = state[7] = 1 / math.sqrt(2)
        previous = 0
        for index, (time, sensor) in enumerate(records):
            rotate_signal(state, weights, frequency, time - previous)
            state = [state[basis ^ (1 << sensor)] for basis in range(8)]
            if index < budget:
                state = [state[basis ^ (1 << sensor)] for basis in range(8)]
            previous = time
        rotate_signal(state, weights, frequency, duration - previous)
        parity = sum(state[basis ^ 7].conjugate() * (1j if basis % 2 == 0 else -1j)
                     * amplitude for basis, amplitude in enumerate(state))
        exposure, signs, _ = apply_policy(records, duration, (duration,) * 3,
                                          weights, budget)
        assert abs(parity.imag) < 1e-12
        assert math.isclose(signs[0] * parity.real, math.sin(frequency * exposure),
                            abs_tol=1e-12)
    print("Three-qubit circuit: corrected X/Y parity agrees with the signed-exposure phase")


def knapsack_optimum(weights, rates, budget_rate):
    remaining = budget_rate
    allocation = [0.0] * len(weights)
    for sensor in sorted(range(len(weights)), key=lambda index: weights[index] / rates[index],
                         reverse=True):
        allocation[sensor] = min(1, remaining / rates[sensor])
        remaining -= rates[sensor] * allocation[sensor]
        remaining = max(0, remaining)
    return allocation


def check_heterogeneous_allocation():
    weights, rates = (2, 0.7, 3), (5, 1, 2)
    for budget_rate in (0, 0.5, 2, 2.2, 5.6, 8, 10):
        allocation = knapsack_optimum(weights, rates, budget_rate)
        value = sum(weight * fraction for weight, fraction in zip(weights, allocation))
        dual = min(multiplier * budget_rate
                   + sum(max(0, weight - multiplier * rate)
                         for weight, rate in zip(weights, rates))
                   for multiplier in (0, *(weight / rate for weight, rate
                                          in zip(weights, rates))))
        assert math.isclose(value, dual, abs_tol=1e-12)

    weights, rates = (1, 1), (1, 3)
    assert knapsack_optimum(weights, rates, 1) == [1, 0]
    duration, budget = 200, 200
    slack = 0.85
    windows = ((slack * duration, 0), (slack * duration / 4,) * 2)
    generator = random.Random(20261128)
    samples = [[], []]
    for _ in range(600):
        records = sample_records(generator, rates, duration)
        for protected, results in zip(windows, samples):
            exposure, _, corrections = apply_policy(records, duration, protected,
                                                    weights, budget)
            assert corrections <= budget
            results.append((exposure / duration)**2)
    for protected, results in zip(windows, samples):
        moments = [telegraph_moments(duration - time, rate)
                   for time, rate in zip(protected, rates)]
        means = [time + moment[0] for time, moment in zip(protected, moments)]
        variances = [second - mean**2 for mean, second in moments]
        unclipped = (sum(means)**2 + sum(variances)) / duration**2
        estimate, error = average_and_error(results)
        assert abs(estimate - unclipped) < 5 * error
    ratio = statistics.fmean(samples[0]) / statistics.fmean(samples[1])
    assert 3.7 < ratio < 4.1
    print(f"Heterogeneous policy: asymptotic ratio 4; finite simulated ratio {ratio:.4f}")


def delayed_moments(duration, rate, delay):
    attenuation = math.exp(-2 * rate * delay)
    boundary = min(duration, delay)
    mean, second = telegraph_moments(boundary, rate)
    if duration <= delay:
        return mean, second
    mean += attenuation * (duration - delay)

    def inner_moment(time):
        if time <= delay:
            return telegraph_moments(time, rate)[0]
        # Integrate exp(-2γ times the window symmetric difference) over earlier times.
        separated = max(0, time - 2 * delay)
        ramp_start = max(0, time - delay)
        before_overlap = attenuation * telegraph_moments(min(delay, ramp_start), rate)[0]
        startup_overlap = 0
        if ramp_start < delay:
            length = delay - ramp_start
            startup_overlap = math.exp(-4 * rate * (time - delay)) * (
                telegraph_moments(length, rate)[0])
        both_full_overlap = telegraph_moments(min(delay, time - delay), 2 * rate)[0]
        return (before_overlap + startup_overlap + both_full_overlap
                + separated * attenuation**2)

    return mean, 2 * integrate(inner_moment, duration, panels=12288)


def check_delayed_sign_policy():
    duration, rate, delay = 20, 1.0, 0.5
    generator = random.Random(20261129)
    samples = []
    for _ in range(12_000):
        records = sample_records(generator, (rate,), duration)
        signed, _, _ = apply_policy(records, duration, (duration,), (1,), math.inf, delay)
        samples.append(signed)
    benchmark_mean, benchmark_second = delayed_moments(duration, rate, delay)
    empirical_mean, mean_error = average_and_error(samples)
    empirical_second, second_error = average_and_error([sample**2 for sample in samples])
    assert abs(empirical_mean - benchmark_mean) < 5 * mean_error
    assert abs(empirical_second - benchmark_second) < 5 * second_error
    print(f"Delayed sign policy: E[A]={benchmark_mean:.6f}, E[A²]={benchmark_second:.6f}")


def refresh_basis(basis, scratch_bit):
    controlled_flip = (basis >> 1) & 1
    basis ^= controlled_flip
    if (basis & 1) != ((basis >> scratch_bit) & 1):
        basis ^= 1 | (1 << scratch_bit)
    return basis ^ controlled_flip


def check_coherent_refresh():
    for basis in range(8):
        reference = (basis >> 1) & 1
        sensor = basis & 1
        scratch = (basis >> 2) & 1
        expected = (reference ^ scratch) | (reference << 1) | ((reference ^ sensor) << 2)
        assert refresh_basis(basis, 2) == expected
    variation = max(abs((-1)**(refresh_basis(basis, 2) & 1) - (-1)**(basis & 1))
                    for basis in range(8))
    assert variation / 2 == 1

    # Bit 0 is the sensor, bit 1 the reference and bits 2 and 3 the scratch qubits.
    weights = (1, 0, 0, 0)
    blocks = [[(0.2, 0), (0.7, 0)], [(0.2, 0)], [(0.1, 0), (0.6, 0), (0.9, 0)]]
    total_exposure = sum(apply_policy(records, 1, (0,), (1,), 0)[0]
                         for records in blocks)
    final_sign = (-1)**len(blocks[-1])
    for frequency in (-0.75, 0, 0.31):
        state = [0j] * 16
        state[0] = state[3] = 1 / math.sqrt(2)
        for block_index, records in enumerate(blocks):
            previous = 0
            for time, _ in records:
                rotate_signal(state, weights, frequency, time - previous)
                state = [state[basis ^ 1] for basis in range(16)]
                previous = time
            rotate_signal(state, weights, frequency, 1 - previous)
            if block_index < len(blocks) - 1:
                state = [state[refresh_basis(basis, 2 + block_index)] for basis in range(16)]

        parity = sum(state[basis ^ 3].conjugate() * (1j if basis % 2 == 0 else -1j)
                     * amplitude for basis, amplitude in enumerate(state))
        assert abs(parity.imag) < 1e-12
        assert math.isclose(final_sign * parity.real, math.sin(frequency * total_exposure),
                            abs_tol=1e-12)
    information = total_exposure**2
    assert math.isclose(information, 0.64)

    for rate, delay in itertools.product((0.2, 1, 2), (0.1, 1, 10)):
        best_sign = math.exp(-2 * rate * delay) * min(1, 1 / (rate * delay))
        refresh = telegraph_moments(delay, rate)[0] / delay
        assert refresh > best_sign
    print(f"Coherent refresh: circuit F={information:.6f}, "
          f"long-time coefficient {telegraph_moments(1, 1)[0]**2:.8f} "
          f"vs {math.exp(-4):.8f} for sign-only control at rate and delay 1")


if __name__ == "__main__":
    check_telegraph_and_stopping()
    check_ghz_parity()
    check_heterogeneous_allocation()
    check_delayed_sign_policy()
    check_coherent_refresh()
