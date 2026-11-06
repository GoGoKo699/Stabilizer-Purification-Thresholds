# Scientific account

Stabilizer operations can improve a depolarized unknown qubit once sufficiently many copies are available. The exact minimum is four for a heralded output and five for an output on every run. The constructions work for every target direction over an explicit interval of strong input noise; the lower bounds cover all input polarizations.

Read the account in this order:

1. [Model and exact copy thresholds](model-and-results.md): states, fidelity, success, allowed maps and theorem quantifiers.
2. [Four-copy filtering and a fifth-copy fallback](constructions.md): physical operations, exact gains, success tuning and rational examples.
3. [Heralded converse](heralded-converse.md): why three inputs cannot improve even the accepted-data Haar score.
4. [Deterministic converse](deterministic-converse.md): the four-body stabilizer inequality and why a fourth input is still insufficient without rejection.
5. [Physical interpretation](interpretation.md): directional information, postselection costs and the operational endpoint.

The main theorem combines the constructions with both converses. The [related work](../references/related-work.md) credits the inherited filtering mechanism and two-copy result. The [verification guide](../verification/README.md) supplies reproducible finite checks of the formulas and quantum operations.
