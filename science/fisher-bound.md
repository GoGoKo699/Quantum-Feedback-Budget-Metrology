# Control action and the Fisher-information bound

Consider $`N`$ sensors with signal Hamiltonian $`H_\omega=(\omega/2)\sum_i w_i Z_i`$ and independent, perfectly observed $`X_i`$ jumps of rates $`\gamma_i>0`$. All $`w_i`$ are positive. The initial state may include noiseless ancillas. An in-run coherent control can depend on past jump marks and may react to a new jump immediately after it occurs. Terminal measurements can depend on the full record. The jump record has a parameter-independent law, and the controls are fixed as functions of that record and the nominal frequency.

The charge of an interior unitary $`V`$ at sensor $`i`$ is $`\|V^\dagger Z_iV-Z_i\|/2`$. The corresponding continuous charge for a Hamiltonian $`H_c(t)`$ is $`\tfrac12\int_0^T\|[H_c(t),Z_i]\|\,dt`$. These are operator norms on the joint sensor and ancilla space. The gate and continuous charges sum across sensors and are at most $`B`$ on every jump record. The preparation and terminal POVM are endpoint operations. The bounds below allow arbitrary ancilla dimension, in-run multiqubit unitaries and continuous control chosen from the external record. A model with intermediate measurements and a separate cap on their realized outcomes needs its own cost convention.

## The local derivative along a marked record

Purify the initial state to $`|\psi\rangle`$, granting the final measurement access to that purification for the upper bound. Let $`U_0(t)`$ denote the evolution on a fixed marked record at the nominal frequency, here written as $`\omega=0`$. A different fixed nominal frequency contributes a Hamiltonian commuting with every $`Z_i`$ and does not change the proof. Set

```math
P=I-|\psi\rangle\langle\psi|,\qquad O_i(t)=U_0(t)^\dagger Z_iU_0(t),\qquad
v_i(t)=P O_i(t)|\psi\rangle.
```

The derivative of the time-ordered unitary, with the record held fixed, has input-frame generator $`\tfrac12\sum_i w_i\int_0^T O_i(t)\,dt`$. The pure-state quantum Fisher information of this record's final probe is consequently $`\|\sum_i w_i\int_0^T v_i(t)\,dt\|^2`$. This follows by projecting the state derivative orthogonally to the initial state and multiplying its squared norm by four. The jump process has no classical Fisher information about $`\omega`$, so the classical Fisher information $`F`$ of any allowed terminal readout satisfies

```math
F \le \mathbb E\left\|\sum_i w_i\int_0^T v_i(t)\,dt\right\|^2.
```

Each $`v_i`$ has norm at most one. An uncontrolled jump at sensor $`i`$ sends $`v_i`$ to $`-v_i`$ and leaves the other $`v_j`$ unchanged. A unitary control contributes the difference between the projected, conjugated observables immediately before and after the gate. Its contribution to $`v_i`$ has norm at most $`\|V^\dagger Z_iV-Z_i\|`$. Between jumps and gates, the sensor contribution from the control Hamiltonian has norm at most $`\|[H_c(t),Z_i]\|\,dt`$. Let $`C_i(t)`$ be the sum of these control increments up to time $`t`$. The budget implies $`\sum_i \mathrm{TV}(C_i)\le 2B`$ pathwise.

Write $`N_i(t)`$ for the counting process of physical flips on sensor $`i`$ and $`\widetilde N_i(t)=N_i(t)-\gamma_it`$ for its compensated version. At a jump time use the pre-jump $`v_i(t-)`$ for the physical flip and put any immediate correction in $`C_i`$. This ordering makes the natural-jump integrand predictable even when a control responds without delay. Integrating $`dv_i=-2v_i(t-)\,dN_i(t)+dC_i(t)`$ gives

```math
\gamma_i\int_0^T v_i(t)\,dt
=\frac{v_i(0)-v_i(T)+C_i(T)}2
-\int_0^T v_i(t-)\,d\widetilde N_i(t).
```

## A finite bound and its long-time coefficient

For any threshold $`\lambda\ge 0`$, split $`w_i=\gamma_i h_i+r_i`$ with $`h_i=\min(w_i/\gamma_i,\lambda)`$ and $`r_i=(w_i-\lambda\gamma_i)_+`$. The residual integral contributes at most $`T\sum_i r_i`$ to the norm. The boundary terms in the compensated-count identity contribute at most $`\sum_i h_i`$, and the control terms at most $`\lambda B`$. The martingales from distinct sensor counts are orthogonal in the second moment because the independent compensated counts have no simultaneous jumps. This remains true when every integrand depends on all past marks. The Hilbert-space Poisson isometry gives

```math
\mathbb E\left\|\sum_i h_i\int_0^T v_i(t-)\,d\widetilde N_i(t)\right\|^2
=\sum_i h_i^2\gamma_i\,\mathbb E\int_0^T\|v_i(t-)\|^2\,dt
\le T\sum_i h_i^2\gamma_i.
```

The triangle inequality in mean square now yields the finite bound

```math
\boxed{\sqrt F\le T\sum_i(w_i-\lambda\gamma_i)_++\lambda B
+\sum_i h_i+\sqrt{T\sum_i h_i^2\gamma_i}\qquad(\lambda\ge0).}
```

Taking $`\lambda=0`$ gives the noiseless ceiling $`\sqrt F\le T\sum_i w_i`$. For $`w_i=1`$ and $`\gamma_i=\gamma`$, taking the smaller of the bounds at $`\lambda=0`$ and $`\lambda=1/\gamma`$ gives

```math
\sqrt F\le\min\left\{NT,\frac{N+B}{\gamma}+\sqrt{\frac{NT}{\gamma}}\right\}.
```

With the sensor array fixed and $`B/T\to b`$, take the upper limit of $`\sqrt F/T`$ at each fixed $`\lambda`$. The right-hand side then reduces to the dual of the fractional knapsack problem

```math
G(b)=\max_{\substack{0\le x_i\le1\\\sum_i\gamma_i x_i\le b}}\sum_i w_i x_i
=\inf_{\lambda\ge0}\left[\lambda b+\sum_i(w_i-\lambda\gamma_i)_+\right].
```

To see the equality, order the sensors by decreasing $`w_i/\gamma_i`$, fill their fractions to one in that order, and use a partial fraction on the first sensor that exceeds the remaining allowance. Taking $`\lambda`$ to be the ratio of that sensor gives the allocation's value on the dual side. Tied ratios can share the remaining allowance. The endpoint cases use $`\lambda=0`$ if the allowance covers every sensor and $`\lambda\ge\max_i w_i/\gamma_i`$ if the allowance vanishes. Every admissible control therefore satisfies $`\limsup_{T\to\infty} F/T^2\le G(b)^2`$. The bound holds uniformly over the controls at each $`T`$, so it also applies to their optimum.

## Exact zero-action benchmark

At $`B=0`$ every allowed gate commutes with all $`Z_i`$, and the continuous control commutes with them almost everywhere. Thus $`O_i(t)=q_i(t)Z_i`$, where $`q_i(t)=(-1)^{N_i(t)}`$. Define the integrated signs $`A_i=\int_0^T q_i(t)\,dt`$. Independent Poisson increments give $`\mathbb E q_i(t)=e^{-2\gamma_it}`$ and $`\mathbb E[q_i(s)q_i(t)]=e^{-2\gamma_i|t-s|}`$. Integrating these identities yields

```math
a_i=\mathbb E A_i=\frac{1-e^{-2\gamma_iT}}{2\gamma_i},\qquad
d_i=\mathbb E A_i^2=\frac{T}{\gamma_i}-\frac{1-e^{-2\gamma_iT}}{2\gamma_i^2}.
```

For a fixed record the Fisher bound is the variance of $`\sum_i w_i A_i Z_i`$ in the initial state. All pair coefficients in its *averaged* variance are nonnegative because $`\mathbb E[A_iA_j]=a_i a_j`$ for distinct sensors. Each $`Z_i`$ variance and each pair covariance is at most one. A GHZ state saturates all these inequalities at once, and the mark-adjusted local quadrature parity attains its averaged variance. The optimal zero-action value is

```math
F_{B=0}=\sum_i w_i^2 d_i+2\sum_{i\lt j} w_iw_j a_i a_j.
```

For homogeneous sensors this reproduces the GHZ ultimate-information expression of Albarelli, Rossi, Tamascelli and Genoni with their rate convention $`\kappa=2\gamma`$. They reported numerical saturation by perfect photodetection through fourteen sensors. The sign-integral calculation gives exact saturation for the marked Poisson record and optimality over input states under the stated zero-action convention. The homogeneous expression grows as $`N^2`$ at fixed positive $`T`$, and as $`NT/\gamma+O(N^2/\gamma^2)`$ at long time. [Albarelli et al., Quantum 2, 110 (2018), Sec. 3.2, Eq. (19)](https://arxiv.org/html/1803.05891v3#S3.SS2)
