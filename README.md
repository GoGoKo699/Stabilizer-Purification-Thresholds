# Stabilizer Purification Thresholds

How many noisy copies of an unknown qubit are needed to improve its fidelity using only stabilizer operations?

The exact minimum is **four copies with heralding and five copies when every run must return an output**. These thresholds concern the onset of universal fidelity gain: the constructions improve every target direction over an explicit noise interval, while the lower bounds apply at every input polarization.

| Output requirement | Impossible copy budgets | First sufficient budget |
|---|---:|---:|
| Heralded output with positive success | At most 3 | 4 |
| Output on every run | At most 4 | 5 |

The input consists of independent copies of an unknown pure qubit after depolarization,

```math
\rho_{\mathbf u}(r)=\frac{I+r\mathbf u\cdot\boldsymbol\sigma}{2},
\qquad |\mathbf u|=1.
```

Its target-state overlap is $`(1+r)/2`$. The explicit protocols give strict improvement for every direction when

```math
0\lt r\lt \sqrt{-7+2\sqrt{13}}\approx0.45946.
```

The four-copy protocol randomly selects a Pauli basis, measures all four inputs, and accepts unanimous outcomes. Success is at least one eighth. The five-copy protocol returns an untouched fifth input on rejection. For a fixed polarization in the stated interval, four-copy improvement can also be tuned to any prescribed average success strictly below one; at success one the deterministic bound applies.

The converses hold over the full stabilizer Choi cone, including arbitrary completely stabilizer-preserving accepted maps. The attaining protocols use ordinary Pauli measurements and classical control. Copies are counted per attempted batch, and fidelity averages the relevant measurement outcomes. The [model](science/model-and-results.md) states these conventions precisely.

## Read the result

- [Scientific account](science/README.md): the connected route from definitions to physical interpretation.
- [Exact theorem and assumptions](science/model-and-results.md): pointwise universality, average success and the copy budget.
- [Constructions and exact examples](science/constructions.md): accepted filtering, success tuning and deterministic fallback.
- [Heralded converse](science/heralded-converse.md) and [deterministic converse](science/deterministic-converse.md): the matching lower bounds.
- [Related work](references/related-work.md): attribution and comparison with earlier purification results.
- [Verification](verification/README.md): executable checks of the formulas, maps and operator coefficients.

The fixed-axis unanimity filter is inherited from [Gendra et al. (2012)](https://doi.org/10.1088/1367-2630/14/10/105015), and the two-copy no-go was established by [He et al. (2026)](https://doi.org/10.1103/bdw8-k91v). The sharp copy threshold combines the three-copy heralded and four-copy deterministic converses with the physical constructions.

## Learn the project

The educational anchor is **Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information*, 10th Anniversary Edition (2010)**. The [source bridge](learning/nielsen-chuang-bridge.md) connects its treatments of noisy states, quantum operations, fidelity and stabilizer measurements to this project's model and proof mechanisms.

The [30-milestone map](learning/milestones.md) moves from individual states and accepted operations to the complete four-versus-five copy boundary. Its 13 background milestones establish the framework; 17 narrative milestones join the constructions, converse bounds and resource interpretation. The [learning entrypoint](learning/README.md) explains how to use the map alongside the scientific account.

## Reproduce the checks

The [verification guide](verification/README.md) gives the dependencies, commands and expected results for the physical maps, exact operator identities and feasible-point source comparison. The analytic proofs establish the universal bounds; the executable checks verify their algebra and constructions. A separate [hosted mathematics check](verification/hosted/README.md) compares the equations displayed by GitHub with the pinned source.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
