# What the copy threshold measures

The four-versus-five boundary separates two ways of using incomplete information about an unknown qubit. A heralded filter keeps measurement records that provide a stronger directional signal. An unconditional protocol must also supply an output on the rejected records. One untouched noisy copy is enough to cover those failures while retaining the positive gain on accepted runs.

## Stabilizer resources and directional information

The target is the original unknown pure state. The protocol is not asked to create a fixed resource state. Its score measures how well the returned qubit approximates that direction.

In the proved pointwise interval, every input lies inside the single-qubit stabilizer octahedron. Indeed, a Bloch vector $`r\mathbf u`$ is in that octahedron when its component absolute values sum to at most one, and $`r\sum_a|u_a|\le r\sqrt3\lt 1`$. The accepted outputs are mixtures of Pauli eigenstates. Universal improvement in this regime therefore does not require nonstabilizer inputs or outputs.

This observation explains the role of the task: several weak signals about an unknown direction can improve its estimate and the prepared approximation. The stabilizer restriction still matters. The converses show that one, two or three inputs cannot give a positive accepted-data Haar gain, and four cannot do so when every run must return an output.

## Postselection and the physical budget

The bare four-copy protocol consumes four noisy specimens on every attempted batch. Its success is bounded away from zero uniformly in the target direction, so the gain is not obtained only in a vanishing-success limit. Independent repetition until acceptance costs an expected $`4/p_{\mathbf u}\le32`$ raw specimens for a fixed direction. This is an expectation, not a fixed upper bound on the number consumed in a particular run.

The deterministic protocol consumes five specimens per batch and always returns a qubit. Its gain is smaller because rejected four-copy events contribute only the original fidelity through the fifth input. Thus the number four is the minimum size of an accepted-or-rejected batch, not an assertion that repeating the heralded protocol uses fewer inputs per delivered output than the deterministic construction.

Mixing the filter with returning one input produces arbitrarily high average success below one, but the gain approaches zero as success approaches one. At success exactly one, positive definiteness of the noisy input forces the accepted map to be trace preserving, and the four-copy upper bound applies. The [prescribed-success construction](constructions.md#prescribing-average-success) makes this endpoint precise without claiming an optimal tradeoff curve.

All gates and measurements are ideal. Gate noise, correlated input noise, storage errors on the spare copy and implementation latency require additional modeling. They are not represented by the single input depolarization parameter.

## The role of universal averaging

The pointwise guarantee fixes a target direction first, then averages the accepted classical outcomes and the random choice of Pauli axis. Some individual accepted outcomes are poor approximations to that target. The guarantee concerns the conditional output state, which is the appropriate average for an unobserved target direction and a specified instrument.

The converse uses an easier task: improve the success-weighted Haar score. If every direction improved, this score would improve too. Failure even for that easier task rules out the stronger pointwise requirement. Conversely, a Haar-average gain alone would not prove pointwise gain. This is why the body-diagonal bound is needed in the construction, and why the larger Haar interval is kept separate.

## What closes the theorem

The old unanimity mechanism supplies achievability once its Pauli-axis implementation is written explicitly. The new lower bounds apply to arbitrary coherent maps in the stabilizer Choi cone, not only to local measurement-and-preparation strategies. A state-estimation construction alone cannot establish those converses.

The three-copy argument combines a stabilizer pair-correlation limit with the two endpoint values of an affine polynomial in $`r^2`$. The four-copy deterministic argument uses an additional four-body correlation that trace preservation forces to vanish. These are the exact restrictions that meet the four- and five-input constructions.

The theorem closes the minimum-copy question at its stated onset. It leaves the full fidelity-versus-success frontier and the behavior at other polarizations as distinct questions. The [related-work account](../references/related-work.md) explains how this scope relates to estimation with abstention and to existing two-copy resource laws.
