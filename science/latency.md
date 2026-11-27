# What feedback delay changes

Let $`\delta\ge0`$ be a fixed reporting delay. At time $`t`$ an interior control sees only the marked Poisson record through $`(t-\delta)_+`$. The terminal measurement may use the completed record. For the attaining protocols the fixed Pauli measurements can be made at the endpoint, followed by record-dependent classical processing. Waiting for the last report adds at most $`\delta`$ to wall time, which leaves the fixed-delay long-time limits unchanged. The sensor Hamiltonian, rates and hard action cap are those in the [Fisher-information bound](fisher-bound.md).

## Exact allocation with sign controls

A sign control sends each physical $`Z_i`$ to $`+Z_i`$ or $`-Z_i`$ by conjugation. A reversed sign costs one action on that sensor. Local $`X_i`$ corrections are an example. Multiqubit gates are allowed if they have this action on every $`Z_i`$. Controls may depend on all delayed external marks, with arbitrary initial probes and noiseless ancillas and an arbitrary record-dependent terminal measurement.

Write $`F^*_{\delta,\mathrm{sign}}(T,B)`$ for the supremum of the attainable local Fisher information with this restricted control class. For fixed sensor array, fixed $`\delta`$, and $`B/T\to b`$,

```math
\boxed{
\lim_{T\to\infty}\frac{F^*_{\delta,\mathrm{sign}}(T,B)}{T^2}
=G_\delta(b)^2,qquad
G_\delta(b)=
\max_{\substack{0\le x_i\le1\\\sum_i\gamma_i x_i\le b}}
\sum_i w_i e^{-2\gamma_i\delta}x_i .
}
```

Thus the optimal priority within this class is $`w_i e^{-2\gamma_i\delta}/\gamma_i`$. The ranking can change even when all sensor parameters are known. For example, take $`(w_1,\gamma_1)=(1,1)`$ and $`(w_2,\gamma_2)=(3,2)`$ in consistent units. Sensor 2 is first at zero delay. Sensor 1 becomes first for $`\delta>\tfrac12\log(3/2)`$.

### Why the delay enters as a weight

Let $`K_i(t)`$ count sign reversals due to controls, and let $`\mathcal F_s`$ contain all external marks through time $`s`$ and any independent classical seed used by the controller. The sign of the dressed observable $`U_0(t)^\dagger Z_i U_0(t)`$ is

```math
q_i(t)=(-1)^{N_i(t)+K_i(t)}.
```

For $`t\ge\delta`$, set $`\widehat q_i(t)=(-1)^{N_i(t-\delta)+K_i(t)}`$ and $`a_i=e^{-2\gamma_i\delta}`$. The controller fixes $`K_i(t)`$ using $`\mathcal F_{t-\delta}`$. The parity of the independent Poisson increment over $`(t-\delta,t]`$ has mean $`a_i`$. Therefore

```math
\mathbb E[q_i(t)\mid\mathcal F_{t-\delta}]=a_i\widehat q_i(t).
```

To control the accumulated residual, choose a pure initial probe and let $`v_i=PZ_i|\psi\rangle`$, with $`P=I-|\psi\rangle\langle\psi|`$ as in the Fisher-information proof. An initial mixed probe can be purified. Define

```math
R(t)=\sum_i w_i\bigl[q_i(t)-a_i\widehat q_i(t)\bigr]v_i,qquad
W=\sum_i w_i .
```

Then $`\|R(t)\|\le2W`$. For $`t-s\ge\delta`$, $`R(s)`$ is $`\mathcal F_{t-\delta}`$-measurable and $`R(t)`$ has zero conditional mean in that information, so their expected inner product vanishes. Integration over the remaining time pairs gives

```math
\mathbb E\left\|\int_\delta^T R(t)\,dt\right\|^2
\le 8W^2 T\delta .
```

The omitted startup interval contributes a norm at most $`W\delta`$. On the shifted clock $`u=t-\delta`$, the signs $`\widehat q_i(u+\delta)`$ obey the zero-delay dynamics with the original rates and control cap, and the signal weights change to $`w_i a_i`$. Any startup sign is an initial sign choice for this shorter problem. Applying the [zero-delay upper bound](fisher-bound.md#a-finite-bound-and-its-long-time-coefficient) and the triangle inequality in mean square gives the upper limit. For $`\delta=0`$, the residual is identically zero.

### Attaining the coefficient

Prepare the GHZ probe and work on the shifted clock. Allocate windows of length $`x_i(T-\delta)`$ by decreasing $`w_i a_i/\gamma_i`$. While a window is active, apply $`X_i`$ on every newly revealed flip, until the hard cap is used up. The new marks drive and correct the shifted signs just as at zero delay. After a window expires, continue recording marks for the terminal readout. A fixed slack in the planned total action rate makes clipping exponentially unlikely for a fixed array as $`T`$ grows, and the slack can tend to zero after taking that limit. The shifted-clock mean signed exposure with weights $`w_i a_i`$ then has coefficient $`G_\delta(b)`$. The integrated residual has sublinear root mean square. The terminal parity uses the actual signed exposure from the full record, including the marks that were unavailable for in-run correction. It attains the stated Fisher-information coefficient without dropping any shots.

## Coherent refresh can do better

Arbitrary coherent controls can exceed the sign-control optimum. One noisy sensor and a noiseless reference suffice for every positive delay. Let the sensor $`s`$ and a noiseless reference qubit $`a`$ start in $`(|0,0\rangle+|1,1\rangle)/\sqrt2`$. At deterministic times $`h,2h,\ldots`$, refresh the sensor using a blank noiseless scratch qubit $`c`$. The following composite instantaneous unitary is a single control in the stated operator-norm convention:

```math
V=\mathrm{CNOT}_{a\to s}\;\mathrm{SWAP}_{s,c}\;
\mathrm{CNOT}_{a\to s}.
```

An interval's net $`X`$ error $`e`$ is the sensor's bitwise difference from the reference. On either computational basis branch the gate acts as $`|j,j\oplus e,0\rangle\mapsto|j,j,e\rangle`$, restoring the sensor and retaining the accumulated relative phase. The scratch qubit stores only $`e`$. As an operator identity, $`V^\dagger Z_s V=Z_aZ_c`$, so the refresh costs $`\|Z_aZ_c-Z_s\|/2=1`$. Its schedule has no dependence on the marks. Once the full record of a block has arrived, its scratch qubit can be reset from the known bit $`e`$ by an ancilla-only operation that leaves $`Z_s`$ unchanged. At most $`\lceil\delta/h\rceil+2`$ scratch qubits suffice with this recycling.

For unit signal weight, the signed exposure from a complete block is an independent integral of a fresh telegraph sign. Its mean is $`m(h)=(1-e^{-2\gamma h})/(2\gamma)`$. Given the completed marked record, the final reference and sensor retain the phase determined by the *sum* of these block exposures. Measuring the quadrature parity on the reference and sensor gives local Fisher information equal to the expected square of that sum. A last partial block contributes at most $`h`$ to the signed exposure and cannot change the long-time coefficient. With $`\lfloor T/h\rfloor`$ action units available, this gives

```math
\lim_{T\to\infty}\frac{F_{\mathrm{refresh}}(T)}{T^2}
=\left(\frac{1-e^{-2\gamma h}}{2\gamma h}\right)^2 .
```

Taking $`h=\delta>0`$ makes the signed coefficient the average of $`e^{-2\gamma t}`$ over $`0\le t\le\delta`$, strictly larger than $`e^{-2\gamma\delta}`$. The latter is the sign-control coefficient even when the rate allowance covers every revealed flip. Consequently the coherent protocol beats the sign-control optimum at the same finite action rate $`b=1/\delta`$. The comparison uses noiseless ancillary memory and the composite-gate charge specified above. Optimal arbitrary-control performance at positive delay, and resource laws under a fixed elementary gate set, remain open.

The repetition code and periodic parity recovery are standard metrological error correction. Kessler et al. analyze the corresponding syndrome-measurement scheme in a rotated basis, with uncertainty about the jump time within each interval. The benchmark here uses coherent refresh and the completed marked record, and compares its charged long-time coefficient with the sharp delayed sign-control coefficient. [Kessler et al., Phys. Rev. Lett. 112, 150802 (2014)](https://doi.org/10.1103/PhysRevLett.112.150802)
