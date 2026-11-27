# 30 milestones for monitored quantum metrology

Follow one route from a single jump to the optimal allocation of feedback across an array. The first 12 milestones assemble the monitored experiment and its statistical target. The remaining 18 develop the sensing protocol, the converse, and the role of delayed information. Start with the [monitoring bridge](MONITORING_BRIDGE.md) for the educational anchor and a complete two-sensor trajectory.

## Phase I background and preliminaries

### M01 The sign of a qubit signal

**Question.** What does a transverse flip do to a frequency-sensing qubit?

**Target.** Relate the two eigenvalues of $`Z`$ to the phases produced by $`\omega Z/2`$. Use $`XZX=-Z`$ to explain why an $`X`$ changes the sign of subsequent phase accumulation in the frame of the initial basis states.

**Uses.** No earlier milestones. This sign is the local mechanism behind the protocol.

**Read.** [Signal and noise model](../science/model.md).

### M02 GHZ phase accumulation

**Question.** How do several sensors encode one frequency in a single relative phase?

**Target.** Compare the energies of the all-zero and all-one branches under $`(\omega/2)\sum_i w_iZ_i`$. Derive their relative phase $`\omega T\sum_i w_i`$ in the absence of jumps. Explain why known positive weights add coherently.

**Uses.** M01. Moves from a single qubit to a common signal on several sites.

**Read.** [GHZ probe and signed phase](../science/feedback.md#read-the-signed-phase).

### M03 Averaged bit-flip dynamics

**Question.** What does the unconditional open-system equation average over?

**Target.** Obtain $`\gamma_i(X_i\rho X_i-\rho)`$ by mixing the click and no-click maps over a short interval. Identify the environmental information lost in the averaged state.

**Uses.** M01. Introduces the channel that the monitored description resolves into trajectories.

**Read.** [Monitoring anchor, Section II.1.1](MONITORING_BRIDGE.md#educational-anchor) and [project model](../science/model.md).

### M04 Conditioning on a detector click

**Question.** How does a recorded outcome specify the sensor's next state?

**Target.** Apply a click operator to the input state and normalize by its probability. Explain why the normalized branch is a unitary $`X_i`$ for $`L_i=\sqrt{\gamma_i}X_i`$. Relate the normalized state to the click/no-click decomposition of M03.

**Uses.** M03. Turns the unconditional description into an operational record and conditional state.

**Read.** [Monitoring anchor, Section III](MONITORING_BRIDGE.md#educational-anchor) and [project model](../science/model.md).

### M05 Exogenous clocks and informative readout

**Question.** Can a detector record be useful even when its probability law is independent of the signal?

**Target.** Derive the rate $`\gamma_i`$ from $`L_i^\dagger L_i=\gamma_i I`$. Understand why the Poisson clock of that rate is independent of the unknown frequency and the controls, and why each label and time still matters for interpreting a terminal measurement.

**Uses.** M03–M04. Establishes the separate roles of the classical record and sensor.

**Read.** [Monitoring bridge](MONITORING_BRIDGE.md#educational-anchor) and [project model](../science/model.md).

### M06 Causal order of jump and response

**Question.** If a detector and a control act at the same timestamp, which operation acts first?

**Target.** Write the recorded flip followed by a physical unitary as the joint operator $`V X_i`$. Explain why an immediate $`X_i`$ restores the orientation for later phase accumulation, and why a response based on as-yet-unavailable data would violate the experiment's information boundary.

**Uses.** M04–M05. Defines the allowed timing of the feedback.

**Read.** [Monitoring anchor, Section IV](MONITORING_BRIDGE.md#educational-anchor) and [one trajectory](MONITORING_BRIDGE.md#one-complete-trajectory).

### M07 Signed exposure and final parity

**Question.** Why is the final flip parity alone insufficient to predict the useful phase?

**Target.** Track the parity sign $`q_i(t)\in\{-1,+1\}`$ of physical and corrective flips and integrate $`A=\sum_i w_i\int_0^Tq_i(t)\,dt`$. Compare two trajectories with the same final string and different durations spent at each sign.

**Uses.** M01–M02 and M06. Converts a timed record into the phase $`\omega A`$.

**Read.** [One complete trajectory](MONITORING_BRIDGE.md#one-complete-trajectory) and [feedback construction](../science/feedback.md).

### M08 A local score and Fisher information

**Question.** What does Fisher information measure in one terminal experiment?

**Target.** Recognize the score as the derivative of a log likelihood, and the Fisher information as its second moment. For a binary law of the form $`(1+z\sin(\omega A))/2`$, identify the score $`zA`$ and information $`A^2`$ at the nominal origin.

**Uses.** M07. Ties signed phase to a local statistical quantity.

**Read.** [Parity likelihood and estimator](../science/feedback.md#read-the-signed-phase).

### M09 Averaging over records

**Question.** How do the information values on individual jump histories combine?

**Target.** Factor the joint likelihood into the record law and the conditional terminal law. Because the record law is independent of $`\omega`$, derive the average $`\mathbb E[A^2]`$ for the parity experiment. Contrast it with the information computed after the record is discarded, which can be lower.

**Uses.** M05 and M08. Keeps the same accounting for every run, including budget exhaustion.

**Read.** [Measurement model](../science/model.md) and [protocol and estimator](../science/feedback.md).

### M10 A pure-state information bound

**Question.** What upper bound applies before specifying the terminal measurement?

**Target.** Interpret pure-state quantum Fisher information as four times the squared derivative norm orthogonal to the state, which removes the derivative of an overall phase. Connect the derivative of a controlled unitary trajectory to the integral of the signal generator conjugated by nominal evolution.

**Uses.** M02 and M08–M09. Gives the proof a common bound for arbitrary terminal measurements.

**Read.** [Conditional generator and information bound](../science/fisher-bound.md#the-local-derivative-along-a-marked-record).

### M11 What a unit of control buys

**Question.** Why can a simultaneous operation on several sensors spend several units of control?

**Target.** Read the cost of an instantaneous unitary from its change to each $`Z_i`$ in operator norm. An ideal $`X_i`$ spends one unit. A gate commuting with every $`Z_i`$ spends zero in this model. Recognize the continuous version as the integral of the corresponding commutator norm.

**Uses.** M01 and M10. Gives the converse the same control units as the constructive pulses.

**Read.** [Budget and allowed controls](../science/model.md) and [converse](../science/fisher-bound.md).

### M12 The complete sensing experiment

**Question.** Which operations cost feedback and what information does the experiment report?

**Target.** Assemble preparation, a fixed sensing interval, externally monitored independent clocks, causal control, and terminal record-aware readout. Distinguish a hard per-run cap on interior control from an average over repeat runs. Identify the fixed-array, long-interrogation limit and local frequency target.

**Uses.** M01–M11. Fixes the shared assumptions before comparing the protocol and converse.

**Read.** [Operational model](../science/model.md) and [bridge](MONITORING_BRIDGE.md).

## Phase II narrative and innovation

### M13 A correction policy that respects the cap

**Question.** How can the controller enforce a hard cap on a random stream of jumps?

**Target.** Define protected windows, apply one counterpulse for each eligible jump while a pulse remains, and allow all subsequent jumps without intervention. Explain how the same policy finishes the shot and keeps its measurements when the cap is reached early.

**Uses.** M06–M07, M11–M12. Turns a resource constraint into a complete feedback decision rule.

**Read.** [Feedback protocol](../science/feedback.md#allocate-protected-time).

### M14 Local terminal measurements

**Question.** How can the relative GHZ phase be read using one single-site measurement per sensor?

**Target.** Multiply one $`Y`$ outcome and the remaining $`X`$ outcomes. Use the known final bit on the $`Y`$ site to correct the orientation of the measurement sign. Compute the conditional parity distribution for the worked two-sensor history.

**Uses.** M02, M07–M08, and M13. Translates the conditional phase into a directly measured statistic.

**Read.** [Terminal parity](../science/feedback.md#read-the-signed-phase) and [worked trajectory](MONITORING_BRIDGE.md#one-complete-trajectory).

### M15 A locally unbiased frequency estimator

**Question.** How should shots with different signed exposures enter the estimate?

**Target.** Weight each parity outcome by its signed exposure to obtain the score $`zA`$. Explain how its expectation has derivative $`\mathbb E[A^2]`$ at the nominal origin. With a known normalization, the sample mean score attains the local variance $`1/(\nu\mathbb E[A^2])`$ for $`\nu`$ independent trials.

**Uses.** M08–M09 and M14. Completes the constructive route from input to estimate.

**Read.** [Score estimator](../science/feedback.md#read-the-signed-phase).

### M16 The no-feedback benchmark

**Question.** What information survives if a sensor only records its flips?

**Target.** Connect sign correlation to Poisson parity, $`\mathbb E[q_i(t)q_i(s)]=e^{-2\gamma_i|t-s|}`$. Explain how integrating this correlation yields a leading term linear in $`T`$ at fixed $`N`$. At fixed $`T`$, positive cross-site mean exposures can still give a term quadratic in sensor count.

**Uses.** M05, M07, and M09. Separates the previously known monitored benchmark from the feedback question.

**Read.** [Free-running benchmark](../science/fisher-bound.md#exact-zero-action-benchmark).

### M17 The value of a correction window

**Question.** What does protecting sensor $`i`$ for a fraction $`x_i`$ of the interrogation contribute?

**Target.** Associate long-run phase weight $`w_i x_i`$ with expected pulse rate $`\gamma_i x_i`$. See why an uncontrolled suffix makes a bounded contribution to the mean signed exposure at fixed rates.

**Uses.** M07, M13, and M16. Turns the controller design into an allocation problem.

**Read.** [Allocation and pulse accounting](../science/feedback.md#allocate-protected-time).

### M18 From planned cost to a hard cap

**Question.** Why can a policy planned using expected counts attain a theorem with a strict per-shot cap?

**Target.** Leave fixed positive slack in the planned total pulse rate and clip feedback at the actual cap. Use Poisson concentration to bound the probability of clipping and the bounded signed exposure to control its effect. Send the slack to zero after the long-time limit.

**Uses.** M05, M12–M13, and M17. Justifies using the deterministic allocation under the actual resource contract.

**Read.** [Hard-capped attainment](../science/feedback.md#attain-the-coefficient).

### M19 Toggling-frame signal vectors

**Question.** How does the sign argument generalize to a controller that can rotate or entangle the sensors?

**Target.** Form $`O_i(t)=U(t)^\dagger Z_iU(t)`$ along the known trajectory. Apply it to the input state and project the result orthogonally to the input before taking the derivative norm. At a natural jump on site $`i`$, $`O_i`$ reverses sign. An intervening general unitary can move the corresponding vector by at most the declared action charge times two.

**Uses.** M06 and M10–M11. Lifts the elementary sign mechanism into the all-control proof.

**Read.** [Heisenberg-frame derivation](../science/fisher-bound.md#the-local-derivative-along-a-marked-record).

### M20 Compensating the Poisson count

**Question.** How does a sign-changing jump process lead to a deterministic drift bound?

**Target.** Write a count increment as its mean $`\gamma_i\,dt`$ plus a compensated increment. Separate natural noise jumps from deliberately applied control. Rearrange the resulting evolution to express the integrated signal vector using a boundary difference, a controlled variation term, and a centered stochastic integral.

**Uses.** M05 and M19. Reveals the price of maintaining a mean signal orientation.

**Read.** [Compensated count identity](../science/fisher-bound.md#the-local-derivative-along-a-marked-record).

### M21 Fluctuations and the time scale

**Question.** Why do the centered fluctuations vanish as a fraction of the long-time amplitude?

**Target.** Use the compensated Poisson isometry and the bounded norm of the trajectory vector. Understand why independent channels have no cross bracket and why fluctuations have root-mean-square scale $`\sqrt T`$ for a fixed array. Compare that scale with the $`T`$ scale of the target amplitude.

**Uses.** M10 and M20. Separates the leading controlled effect from stochastic fluctuations.

**Read.** [Finite information bound](../science/fisher-bound.md#a-finite-bound-and-its-long-time-coefficient).

### M22 The same allocation from the converse

**Question.** How can an upper bound for arbitrary controls reproduce a simple greedy rule?

**Target.** At threshold $`\lambda\ge0`$, split $`w_i`$ into $`\min(w_i,\lambda\gamma_i)`$ and $`(w_i-\lambda\gamma_i)_+`$. Apply the actuation bound to the first term and the unit-norm exposure cap to the second. Identify the resulting leading upper bound as the dual to the fractional allocation in M17.

**Uses.** M17 and M19–M21. Matches the general bound to the GHZ construction.

**Read.** [Dual bound and limiting theorem](../science/fisher-bound.md#a-finite-bound-and-its-long-time-coefficient).

### M23 The identical-sensor law

**Question.** What fraction of the noiseless information can a homogeneous array retain?

**Target.** Divide the cap by the expected total number of flips. For a limiting ratio $`\alpha`$, explain why the signed amplitude fraction is $`\min(1,\alpha)`$ and the Fisher-information fraction is its square. Identify why this statement uses a fixed array and increasing time.

**Uses.** M16, M18, and M22. Makes the hard-cap consequence explicit.

**Read.** [Uniform-array bound](../science/fisher-bound.md#a-finite-bound-and-its-long-time-coefficient) and [identical-sensor policy](../science/feedback.md#worked-examples).

### M24 The unequal-sensor law

**Question.** Which sensor should receive the next unit of planned feedback?

**Target.** Sort by $`w_i/\gamma_i`$ and fill the protection fractions in that order. For equal weights, rates 1 and 3, and a budget rate of 1, compare $`(x_1,x_2)=(1,0)`$ with equal protected time. Their local information coefficients are 1 and $`1/4`$ under the same pulse-rate limit.

**Uses.** M17–M18 and M22–M23. Interprets the matching theorem as an allocation decision.

**Read.** [Heterogeneous feedback](../science/feedback.md#worked-examples) and [optimality](../science/fisher-bound.md#a-finite-bound-and-its-long-time-coefficient).

### M25 The latency information boundary

**Question.** What may a delayed controller know while the phase is accumulating?

**Target.** At time $`t`$, separate the jump record through $`t-\delta`$ from the recent jumps in $`(t-\delta,t]`$. The phase readout can still use the full record after sensing. Keep its terminal information distinct from what the controller can use to choose interior operations.

**Uses.** M05–M06 and M12. Precisely states the change to the immediate-monitoring interface.

**Read.** [Delayed control model](../science/latency.md).

### M26 Recent flip parity under delayed correction

**Question.** What sign remains uncertain when every eligible flip receives a delayed response?

**Target.** For the fully protected interior of a scheduled window, cancel all physical flips older than $`\delta`$. The remaining sign is the parity of flips in the recent interval. Its mean is $`e^{-2\gamma_i\delta}`$, which multiplies the long-time signal weight attained by the delayed policy.

**Uses.** M16–M17 and M25. Derives the cost of leaving noise uncorrected during the response delay.

**Read.** [Delayed protocol and parity](../science/latency.md#why-the-delay-enters-as-a-weight).

### M27 Allocating feedback with latency

**Question.** How does a fixed delay change the priority order?

**Target.** Work out the corrected-window value $`w_i e^{-2\gamma_i\delta}`$ and compare it to the same pulse rate $`\gamma_i`$. With weights $`(1,4)`$ and rates $`(1,3)`$, the second sensor has priority at zero delay, while the first has priority at $`\delta=0.1`$ in matching time units. Read the assumptions of the delayed converse before transferring this rule to other controllers.

**Uses.** M18, M22, and M25–M26. Connects the changed record interface to a changed controller.

**Read.** [Delayed allocation and converse](../science/latency.md#exact-allocation-with-sign-controls).

### M28 A coherent refresh on a fixed schedule

**Question.** How can an ancillary reference restore the sensor before the latest mark is available?

**Target.** Follow the periodic operation $`|j,j\oplus e,0\rangle\mapsto|j,j,e\rangle`$. The scratch stores the error bit $`e`$ without distinguishing the two logical branches $`j`$. Compare the mean telegraph sign across a refresh interval of length $`\delta`$ with the delayed sign policy's mean $`e^{-2\gamma\delta}`$. Explain how the coherent operation achieves a strictly greater coefficient with the stated cost for the composite gate.

**Uses.** M11, M16, and M25–M27. Establishes where the delayed sign-control optimum stops applying.

**Read.** [Coherent refresh and its cost](../science/latency.md#coherent-refresh-can-do-better).

### M29 Checking the protocol and its physical scope

**Question.** What do the finite checks verify, and what would an experimental test need?

**Target.** Compare the stopping-time calculation for identical sensors with simulations that draw explicit jump histories. Identify the device assumptions each check inherits, including known rates, exact time labels, reliable site actuation, and a local operating point. Distinguish the study's interior control budget from detection, calibration, preparation, and measurement costs. Explain what additional localization guarantee would be needed for a precision claim across a fixed frequency band.

**Uses.** M07, M12–M16 and M24–M28. Connects the finite checks, theorem, and a possible device.

**Read.** [Verification](../verification/README.md) and [model and scope](../science/model.md).

### M30 The complete scientific story

**Question.** What does feedback accomplish that an error record alone cannot accomplish?

**Target.** Explain how the record labels past signs, while a paid physical action changes future signs. Reconstruct the chain from sign correction and local parity readout through Poisson drift and the allocation dual. Distinguish the exact immediate and delayed sign-control limits, the attainable coherent delayed coefficient, and the open problem of optimal coherent control with positive delay.

**Uses.** M12–M29. Integrates the result, its strongest proof idea, and its operational limits.

**Read.** [Project model](../science/model.md), [protocol](../science/feedback.md), [converse](../science/fisher-bound.md), and [latency](../science/latency.md).
