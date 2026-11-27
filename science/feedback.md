# Pulse allocation and local estimation

## Allocate protected time

For a fixed array and an asymptotic action rate $`b`$, a fraction $`x_i`$ of protected time on sensor $`i`$ offers signal $`w_i x_i`$ and requires mean action rate $`\gamma_i x_i`$. Sort sensors by decreasing $`w_i/\gamma_i`$. Fill $`x_i`$ to one in that order until the allowance is used, using a partial last interval if necessary. Moving a little action from a lower ratio to a higher unsaturated ratio increases protected signal. This exchange proves that the order solves the [allocation problem](model.md#what-is-optimized).

Choose the scheduled mean action rate slightly below the hard rate. Prepare

```math
|\mathrm{GHZ}\rangle=\frac{|0^N\rangle+|1^N\rangle}{\sqrt{2}} .
```

On site $`i`$ correct each marked bit flip occurring inside $`[0,x_iT]`$ with an immediate physical $`X_i`$. Stop correcting across the entire array when the hard cap is exhausted. Continue sensing and logging until $`T`$. Every planned correction costs one action. Independent clocks make the planned count Poisson with mean $`T\sum_i\gamma_i x_i`$. If $`B/T\to b`$ and the planned rate is strictly below $`b`$, the probability of clipping before all planned corrections have been applied decays exponentially in $`T`$. For a noninteger cap use its integer part.

## Read the signed phase

Let $`q_i(t)=+1`$ when the total number of flips on sensor $`i`$ up to time $`t`$, including active corrections, is even, and $`q_i(t)=-1`$ otherwise. The sign multiplies the instantaneous signal in the frame of the first GHZ component. The accumulated signed exposure is

```math
A=\sum_i w_i\int_0^T q_i(t)\,dt .
```

The complete record gives both $`A`$ and the final bit string $`c`$ of that component. The conditional state is

```math
|\psi_{\omega,c}\rangle=\frac{
e^{-i\omega A/2}|c\rangle+e^{i\omega A/2}|\bar c\rangle}{\sqrt2}.
```

Measure $`Y`$ on site 1 and $`X`$ on the other sites. Multiply the product of the outcomes by $`(-1)^{c_1}`$ to obtain a parity $`z\in\{-1,+1\}`$. Conditional on the record,

```math
p(z\mid A)=\frac{1+z\sin(\omega A)}2 .
```

At the nominal origin the score is $`zA`$, so the records and parity have Fisher information $`\mathbb E A^2`$. The value equals the mean conditional quantum Fisher information. With $`m`$ independent experiments, the local estimator

```math
\widehat{\omega}=\frac{\sum_{j=1}^m z_j A_j}{m\,\mathbb E A^2}
```

has zero mean at the nominal origin, unit slope of its mean there and variance $`1/(m\,\mathbb E A^2)`$ there whenever $`\mathbb EA^2>0`$. The normalization follows from the known noise and policy or can be evaluated by simulation; the exact expression above uses its true value. The terminal outcomes suffice without undoing the final flips on the sensors.

## Attain the coefficient

For the unclipped policy, each protected interval contributes its full duration. Once protection ends, a free-running sign starting at $`+1`$ has mean $`e^{-2\gamma_i t}`$ after duration $`t`$. Its mean additional exposure is bounded by $`1/(2\gamma_i)`$. Replacing the unclipped policy by the hard-capped one changes $`A/T`$ by at most $`2\sum_iw_i`$ on the clipping event. Consequently

```math
\lim_{T\to\infty}\frac{\mathbb EA}{T}=\sum_iw_ix_i .
```

Jensen's inequality gives the square of this quantity as a lower bound on the limiting Fisher coefficient. Take the slack in the allocation to zero after taking the long-time limit. The [upper bound](fisher-bound.md) gives the same coefficient. At zero rate it gives a zero quadratic coefficient and the [zero-action formula](fisher-bound.md) still supplies the finite information.

## Worked examples

For two sensors of unit signal strengths and rates one and three, one unit of action per unit time buys complete protection of the quieter sensor in the limit. This gives Fisher coefficient $`1`$ in units of $`T^2`$. Equal protected fractions give $`x_1=x_2=1/4`$ and coefficient $`1/4`$. Both policies use the same cap with arbitrarily small slack. The noiseless coefficient is $`4`$.

For identical sensors, a simple finite policy corrects all marks until it has applied $`B`$ pulses. The time of the last paid correction has the Gamma law with integer shape $`B`$ and rate $`N\gamma`$, for $`B\ge 1`$. The protected exposure before that time is deterministic conditional on it. The free-running suffix starts with all signs positive, so independent telegraph moments evaluate the remaining information. For four sensors with unit rate interrogated for ten time units, the information is about $`41.000`$ at zero pulses, $`520.788`$ at a hard cap of twenty, and $`1474.492`$ at a cap of forty. The noiseless ceiling is $`1600`$. See the [finite calculations](../verification/README.md).
