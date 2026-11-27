# Reproduce the finite checks

From the repository root, run

```sh
python3 verification/run_checks.py
```

The script uses the Python standard library and fixed random seeds. It prints the quadrature results, simulation estimates and circuit checks. It typically runs in a few seconds.

## Zero and finite feedback budgets

The script obtains the free-running telegraph moments from their defining integrals and checks the resulting GHZ information against Eq. (19) of Albarelli et al., with $`\kappa=2\gamma`$. It evaluates the finite-budget policy by integrating over the Gamma-distributed arrival time of the last allowed correction and including the probability that the cap is never reached. An independent simulation generates per-sensor exponential waiting times, merges the marked records, and integrates the actual sign on each sensor. [Albarelli et al.](https://arxiv.org/pdf/1803.05891)

For four identical sensors with $`\gamma=1`$ and $`T=10`$, the script produces the results below. The simulation uses 30,000 records. Parentheses contain one estimated standard error.

| Per-run pulse cap | Information by quadrature | Simulation |
| ---: | ---: | ---: |
| 0 | 41.000000 | 40.9532 (0.3295) |
| 20 | 520.788003 | 520.4612 (1.5407) |
| 40 | 1474.492044 | 1473.7752 (1.2102) |

The noiseless information is 1600. A direct three-qubit state-vector calculation checks the corrected local $`X/Y`$ parity at multiple frequencies and feedback budgets. [Feedback protocol](../science/feedback.md) · [Information bound](../science/fisher-bound.md)

## Heterogeneous feedback and finite latency

The script compares the greedy allocation with the dual bound at several budget rates. For two equal signal weights and flip rates 1 and 3, it also simulates both the prioritized policy and the equal-time policy under the same hard cap. With $`T=200`$, cap 200, and the same 15% allocation slack, the finite simulated information ratio is 3.8821. The ratio tends to 4 for the two asymptotic policy coefficients as the slack vanishes.

For a single sensor with $`\gamma=1`$, $`T=20`$ and delay $`\delta=0.5`$, the simulated delayed corrections agree with exposure moments computed from the overlap of recent-flip windows. The calculated mean is 7.489709 and the second moment is 61.982110.

A separate state-vector calculation checks the coherent refresh on all eight basis inputs, including its unit chord action. Two refreshes preserve the sum of the signed exposures over three sensing blocks, and a fixed reference-and-sensor quadrature parity with record-dependent sign attains the conditional information 0.64 in the checked branch. With rate and delay both equal to 1, this protocol's long-time coefficient of $`T^2`$ is 0.18691127, compared with 0.01831564 for optimal sign-only control under the same action budget. [Latency analysis](../science/latency.md)

The finite checks test the stated examples and implementations. The general converse and long-time limits follow from the analytical arguments.
