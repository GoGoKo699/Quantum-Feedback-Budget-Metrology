# From monitored jumps to a feedback budget

Start with a sensor that accumulates a phase proportional to an unknown frequency. A transverse bit flip reverses the sign of later phase accumulation. The time of the flip tells us which sign was active, and a physical counterpulse can restore the sign for the rest of the interrogation. The project asks what an experiment can recover when this second operation has a hard limit on every run.

## Educational anchor

Francesco Albarelli and Marco G. Genoni, *A pedagogical introduction to continuously monitored quantum systems and measurement-based feedback*, **Physics Letters A 494**, 129260 (2024). The links follow the accessible author version, **arXiv:2312.13214v1**. [Author version](https://arxiv.org/html/2312.13214v1) · [Published article](https://doi.org/10.1016/j.physleta.2023.129260)

| Where to read | What to carry into the project |
| --- | --- |
| Section II.1.1, Lindblad master equation | The dissipator describes dynamics after averaging over possible environmental outcomes. |
| Section III, photodetection subsection and the Kraus form in Eqs. (80)–(81) | The same physical model has separate click and no-click transformations. The click rate is generally a state-dependent expectation of the jump operator squared. |
| Section IV, continuous photodetection feedback, Eqs. (83)–(89) | The response follows the detected jump. The combined jump-and-response operation is the product of the feedback unitary and the jump operator, in that order. |

The local model sets the anchor's detection efficiency $`\eta=1`$ and takes its collapse operator $`\hat c`$ to be a Pauli $`X_i`$ with rate $`\gamma_i`$ in place of $`\kappa`$. Since $`X_i^\dagger X_i=I`$, the click intensity is $`\gamma_i`$ for every sensor state and signal value. Each click is a unitary flip after normalization. The independent channels supply independent, time-stamped site labels. Conditional on these labels, free evolution and any applied controls are ordinary unitaries. [Project model](../science/model.md)

The project uses this representation to optimize how much information an experiment retains about the frequency. Its additional steps are to compute the record-dependent phase, derive a converse for budgeted controls, and solve the allocation of correction time across sensors. [Phase measurement and protocol](../science/feedback.md) · [Fisher-information converse](../science/fisher-bound.md)

## One complete trajectory

Use two equally weighted sensors, the input $`(|00\rangle+|11\rangle)/\sqrt{2}`$, and an interrogation lasting four time units. Suppose sensor 1 flips at time 1 and sensor 2 flips at time 3. The signal Hamiltonian is $`\omega(Z_1+Z_2)/2`$. For a sensor's first computational branch, a plus sign means that the contribution to the difference between the two branches' phases increases at rate $`\omega`$. A minus sign reverses that contribution.

| Time | Physical event | Signs with one correction available |
| --- | --- | --- |
| $`0\le t<1`$ | Free interrogation | $`(+1,+1)`$ |
| $`t=1`$ | The controller uses its pulse immediately after the recorded flip of sensor 1 | $`(+1,+1)`$ after the pulse |
| $`1<t<3`$ | Free interrogation | $`(+1,+1)`$ |
| $`3\le t\le4`$ | The recorded flip of sensor 2 remains uncorrected | $`(+1,-1)`$ |

The signs integrate to $`4`$ and $`2`$, so the signed exposure is $`A=6`$. The record includes both flips, even after the controller spends its pulse. The final pair of basis states is $`|01\rangle,|10\rangle`$, and the conditioned state is

```math
\frac{e^{-3i\omega}|01\rangle + e^{3i\omega}|10\rangle}{\sqrt{2}}.
```

Measuring $`Y_1`$ and $`X_2`$ and multiplying the outcomes gives a parity $`z\in\{-1,+1\}`$ with $`\Pr(z\mid\text{record})=[1+z\sin(6\omega)]/2`$. The classical Fisher information of this parity at $`\omega=0`$ is $`36`$. With zero control pulses and the same marks, the signed exposures would have been $`-2`$ and $`2`$. The terminal record would still identify the final basis states, even though the phase would have canceled.

Actual timestamps are random. This trajectory explains one conditional value. The experimental information is the mean of the squared signed exposure over all records, including those that exhaust the pulse cap. The fixed-time, zero-feedback benchmark and the long-time interrogation budget answer distinct experimental questions. [Protocol and estimator](../science/feedback.md) · [Finite reproduction](../verification/README.md)

## Follow the research argument

1. [Milestones M01–M12](MILESTONES.md#phase-i-background-and-preliminaries) build the instrument, record, signed exposure, and resource definitions.
2. [Milestones M13–M24](MILESTONES.md#phase-ii-narrative-and-innovation) derive the receiver and estimator, then compare the constructive allocation with the upper bound for all admissible coherent controls under immediate monitoring.
3. [Milestones M25–M30](MILESTONES.md#m25-the-latency-information-boundary) use the delayed record model, coherent refresh, and the finite checks to interpret the theorem's experimental scope.
