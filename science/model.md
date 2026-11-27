# Model and results

Consider a fixed array of qubit sensors. Sensor $`i`$ couples to the unknown frequency $`\omega`$ with known strength $`w_i>0`$, and its bath causes bit flips at a known rate $`\gamma_i>0`$. With no controls the reduced master equation is

```math
\dot\rho=-i[H_\omega,\rho]+\sum_{i=1}^N\gamma_i(X_i\rho X_i-\rho),
\qquad H_\omega=\frac{\omega}{2}\sum_{i=1}^N w_i Z_i .
```

We fix the monitoring instrument. Every jump is the unitary $`X_i`$ and produces a classical mark identifying $`i`$ and the physical event time. The identity $`(\sqrt{\gamma_i}X_i)^\dagger(\sqrt{\gamma_i}X_i)=\gamma_i I`$ makes these marked processes independent Poisson clocks for every input, frequency and control, with normalized no-jump evolution unitary. There is no coherent access to the bath or choice of another measurement of it. The controller has the marks as they occur in the zero-delay model. In the delay model it receives a physical mark from time $`s`$ at time $`s+\delta`$. At readout the experiment waits, if needed, to collect the full record of marks generated during the interrogation.

## What is charged

The protocol chooses an initial sensor–ancilla state, runs one interrogation of length $`T`$, and makes a terminal measurement with access to the entire external record. Any noiseless ancilla is independent of the noise and the signal. In-run controls are parameter-independent coherent operations that may depend causally on received marks and independent classical randomness. We admit bounded-piecewise continuous controls with integrable commutators and instantaneous operations with finite total action, with coincident feedback ordered after its triggering mark. A terminal measurement follows sensing and so cannot act back on the interrogation.

For an instantaneous control $`V`$, use the operator-norm cost in the table. A gate acting in parallel pays the sum over the sensors whose $`Z_i`$ observables it changes. Continuous drive is charged by the time integral of its commutator with each such observable.

| In-run action | Cost on site $`i`$ |
| --- | --- |
| Control $`V`$ | $`\tfrac12 \lVert V^\dagger Z_i V-Z_i\rVert`$ |
| Continuous drive $`H_c(t)`$ | $`\tfrac12\int_0^T\lVert[H_c(t),Z_i]\rVert\,dt`$ |
| Ideal instantaneous bit flip $`X_i`$ | $`1`$ |
| Ancilla-only operation or a gate commuting with $`Z_i`$ | $`0`$ |

The total action is at most $`B`$ on every run. It is a bound on changes to the physical signal observables. There is no charge in this model for initial preparation, terminal measurement, classical computation, detector operation or noiseless ancilla-only gates. The ideal instantaneous rotation and a continuous implementation can have different charges. The converse covers continuous drive with the stated charge, and the sharp construction uses instantaneous $`X_i`$ pulses.

## What is optimized

Write $`F_{\mathrm{opt}}(T,B)`$ for the supremum of local Fisher information in the complete record and measurement outcome, evaluated at a known nominal frequency. One may set that nominal frequency to zero by a commuting compensation field, which has zero action under this convention. There is no Fisher information in the mark law itself, so the score comes from the conditional terminal outcomes. Runs with many jumps still count and still provide terminal data. The local criterion does not address frequency aliases or localization on a fixed nonshrinking band.

For fixed $`N`$ and fixed positive rates and couplings, let $`B/T\to b`$ as $`T\to\infty`$. Then

```math
\lim_{T\to\infty}\frac{F_{\mathrm{opt}}(T,B)}{T^2}=G(b)^2,
\qquad
G(b)=\max_{\substack{0\le x_i\le 1\\ \sum_i\gamma_i x_i\le b}}
\sum_i w_i x_i .
```

The variables $`x_i`$ are fractions of protected time. An optimal allocation fills sensors in order of decreasing $`w_i/\gamma_i`$, with partial protection on the last sensor if needed. The upper bound allows arbitrary coherent controls and noiseless ancillas in the stated model. The attaining scheme uses a GHZ state, marked $`X_i`$ corrections, and local Pauli measurements.

With delay $`\delta`$, the sharp law within the class of controls preserving each physical $`Z_i`$ up to sign uses weights $`w_i e^{-2\gamma_i\delta}`$ in the same optimization. A coherent reset using an ancilla can exceed that restricted optimum. See the [delay theorem and separation](latency.md).

## Reading order

1. [The allocation and estimator](feedback.md) show exactly which pulses to apply and what the resulting measurement estimates.
2. [The converse](fisher-bound.md) explains why coherent control cannot do better at zero delay.
3. [Feedback latency](latency.md) gives the sharp sign-preserving law and what changes when coherent controls are available.
4. [Related work](../references/RELATED_WORK.md) and [finite checks](../verification/README.md) record attribution and validation.
