# Quantum Feedback Budget Metrology

**How much control does a quantum sensor need when it knows exactly when its errors occurred?** We study qubit sensors whose bit flips are tagged by sensor and time. A flip reverses the sign of the frequency signal. The record tells the experimenter when the sign changed, and feedback can keep the signal accumulating in the same direction.

For a fixed array, let $`w_i`$ be the signal strength of site $`i`$, $`\gamma_i`$ its flip rate, and $`b`$ the allowed control action per unit time. At zero feedback delay, the optimal long-time local Fisher information is

```math
\lim_{T\to\infty}\frac{F_{\mathrm{opt}}(T,B)}{T^2}
=\left[
\max_{\substack{0\le x_i\le1\\ \sum_i\gamma_i x_i\le b}}
\sum_iw_ix_i
\right]^2,\qquad B/T\to b .
```

The GHZ protocol protects sites in order of decreasing $`w_i/\gamma_i`$, stops applying corrections at the hard cap, and uses the full record in a final parity measurement. For identical sensors, a cap equal to a fraction $`\alpha`$ of the mean number of flips preserves the fraction $`\min(1,\alpha)^2`$ of the noiseless information. For two equally sensitive sensors with flip rates one and three, prioritizing the quieter sensor gives **four times** the long-time information of equal protected time at the same cap.

| Question | Result |
| --- | --- |
| What is the limit at zero feedback delay? | The allocation law is sharp against arbitrary causal coherent controls and noiseless ancillas under the stated action charge. |
| How does delayed pulse feedback change the allocation? | For controls preserving each $`Z_i`$ up to sign, the sharp rule replaces $`w_i`$ by $`w_i e^{-2\gamma_i\delta}`$ at delay $`\delta`$. |
| Can coherent control beat the delayed pulse rule? | Yes. An explicit sensor–ancilla refresh exceeds the entire sign-preserving class at the demonstrated matching budget. |

## Read the science

| To inspect | Read |
| --- | --- |
| Monitoring, hard cap, local criterion and theorem | [Model and results](science/model.md) |
| Pulse priorities, explicit parity estimator and finite examples | [Protocol](science/feedback.md) |
| Compensated-jump proof and the no-feedback benchmark | [Fisher-information bound](science/fisher-bound.md) |
| Delayed marks, revised priorities and a coherent separation | [Feedback latency](science/latency.md) |
| Established ingredients and related sensing models | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Commands and numerical checks | [Verification](verification/README.md) |

The proof uses an ideal instrument with independent, perfectly observed jumps and a hard bound on changes to the physical signal observables. State preparation, classical mark processing and terminal readout are supplied. The information is local to a nominal frequency. The sharp positive-delay law for arbitrary coherent controls remains open.

## Learn the project

The educational anchor is Francesco Albarelli and Marco G. Genoni's *A pedagogical introduction to continuously monitored quantum systems and measurement-based feedback* (2024). The [monitoring bridge](learning/MONITORING_BRIDGE.md) connects the tutorial's jump and feedback rules to this model. The [30 milestones](learning/MILESTONES.md) develop the protocol, converse and delay results in order. The [reading guide](llms.txt) connects specific questions to their source.

## Reproduce the finite checks

From the repository root, run

```sh
python3 verification/run_checks.py
```

The checks use Python's standard library. They test the telegraph benchmark, hard-capped protocol, parity readout, heterogeneous allocation and delayed-control examples. The general and asymptotic statements follow from the analytical proofs.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
