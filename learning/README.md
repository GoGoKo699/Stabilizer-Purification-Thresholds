# Learning route

How many noisy copies of an unknown qubit are needed before stabilizer processing can improve its fidelity for every target direction? This project finds the exact onset: **four inputs with heralding and five inputs when every batch must return an output**. The distinction concerns the smallest batch that permits a strict improvement somewhere in the noisy-input domain, with an explicit common interval of pointwise improvement.

The single educational anchor is Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information*, **10th Anniversary Edition (2010)**. The [publisher record](https://doi.org/10.1017/CBO9780511976667) and [official contents](https://assets.cambridge.org/97811070/02173/toc/9781107002173_toc.pdf) identify the edition and section numbering. Its treatment of density operators, quantum operations, fidelity, and stabilizers supplies the foundations. The project supplies the particular correlation inequalities and copy-threshold arguments.

## Route through the material

The [Nielsen–Chuang bridge](nielsen-chuang-bridge.md) identifies the relevant sections and translates their conventions into the project's notation. The [30-milestone map](milestones.md) then connects those foundations to the scientific result. The [scientific account](../science/README.md) contains the canonical statements, constructions, and complete proofs.

The map has two phases, each progressing from individual objects to a connected account:

| Phase | Milestones | Scientific purpose |
|---|---|---|
| Background/preliminaries | M01–M13 | Connect qubit geometry and measurement to conditional maps, stabilizer restrictions, and the weighted universal score. |
| Narrative/innovation | M14–M30 | Connect the filter's mechanism to the two converse arguments, the fifth-copy fallback, and the exact operational boundary. |

The allocation is **13 plus 17** because this project joins several prerequisite descriptions of the same experiment: a Bloch vector, an instrument, a Choi operator, and a collection of stabilizer correlations. Once those descriptions are connected, the research phase can develop the heralded and deterministic converses separately before combining them. Each milestone records a central question, an understanding target, earlier dependencies, a conceptual connection, and source pointers. It is a common map of the science rather than a sequence of full lessons.

## Conventions that carry through the route

- **Unknown direction, identical copies.** For a fixed unknown unit vector $`\mathbf u`$, the inputs are independent copies of $`\rho_{\mathbf u}(r)=(I+r\mathbf u\cdot\boldsymbol\sigma)/2`$. The operation can depend on the known noise parameter $`r`$, but not on $`\mathbf u`$. Averaging over directions describes the comparison criterion; it does not make the directions of the copies independent.
- **Overlap fidelity.** The project uses $`F=\mathrm{tr}(\psi_{\mathbf u}\rho_{\mathrm{out}})`$, with raw-copy benchmark $`F_0=(1+r)/2`$. For a pure target, this is the square of the fidelity convention in Nielsen–Chuang §9.2.2. Squaring a statewise quantity does not commute with averaging it.
- **Accepted-data weighting.** Accepted branches and random axis choices are combined before normalizing the output. The Haar score is $`F^{\mathrm H}=\int p_{\mathbf u}F_{\mathbf u}\,d\mathbf u/\overline p`$, where $`\overline p=\int p_{\mathbf u}\,d\mathbf u`$. A pointwise guarantee holds for this conditional output at each direction, not separately for every classical record.
- **Success is a resource parameter.** The four-copy construction can be adjusted to any prescribed Haar-average success $`0\lt\overline p\lt1`$ throughout its pointwise improvement interval. At $`\overline p=1`$, full rank of the noisy input forces trace preservation, and the four-copy deterministic converse applies.
- **Copy counts refer to batches.** The bare heralded filter consumes four inputs per attempted batch. Repeating fresh attempts at fixed direction has expected cost $`4/p_{\mathbf u}\le32`$, not a fixed maximum cost. The deterministic construction reserves an independent fifth input and counts all five inputs per batch.

These conventions are defined in [model and results](../science/model-and-results.md#inputs-and-fidelity) and explained operationally in [interpretation](../science/interpretation.md).

## Direct routes to the research

| Scientific question | Canonical account | Map connection |
|---|---|---|
| What is assumed, and what is the exact theorem? | [Model and results](../science/model-and-results.md) | M13 and M30 |
| How does the accepted operation improve every direction? | [Constructions](../science/constructions.md) | M14–M18 |
| Why are three accepted inputs insufficient? | [Heralded converse](../science/heralded-converse.md) | M19–M22 |
| Why are four inputs insufficient deterministically? | [Deterministic converse](../science/deterministic-converse.md) | M23–M25 |
| How do success probability and physical cost meet? | [Constructions](../science/constructions.md#deterministic-five-copy-operation) and [interpretation](../science/interpretation.md#postselection-and-the-physical-budget) | M26–M28 |
| Which ingredients are inherited, and what remains open? | [Related work](../references/related-work.md) and [scope](../science/model-and-results.md#scope-of-the-threshold) | M29–M30 |

The converse inequalities hold for every $`0\lt r\lt1`$ in the stated class. The displayed constructions improve every direction for

```math
0\lt r\lt r_*:=\sqrt{-7+2\sqrt{13}}\approx0.4594589763.
```

This is a sufficient interval for those constructions. It is not a claim of improvement at every noise strength, optimal fidelity at fixed success, or arbitrarily pure outputs under iteration. The [verification account](../verification/README.md) distinguishes finite checks of the full physical maps from the analytical proofs. Primary research papers in [related work](../references/related-work.md) provide attribution and imported theorem ingredients; Nielsen–Chuang remains the one educational anchor.
