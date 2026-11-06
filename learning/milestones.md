# Thirty milestones for the copy-threshold theorem

This map connects the physical task to its sharp copy thresholds in **exactly 30 milestones**. Phase I contains 13 background/preliminaries milestones; Phase II contains 17 narrative/innovation milestones. The first phase integrates four descriptions of the experiment—qubit geometry, conditional operations, Choi operators, and stabilizer correlations. The second develops the construction and two different converses before joining them into the operational conclusion. Within each phase, the final milestones synthesize the preceding components.

**N&C** means Nielsen and Chuang, *Quantum Computation and Quantum Information*, 10th Anniversary Edition (2010): [publisher record](https://doi.org/10.1017/CBO9780511976667), [official contents](https://assets.cambridge.org/97811070/02173/toc/9781107002173_toc.pdf). It is the sole educational anchor. Its section pointers below identify foundations, not a claim that it contains the project's threshold theorem. The [bridge](nielsen-chuang-bridge.md) translates conventions. Project links identify the canonical statements and locally supplied arguments; the [related-work account](../references/related-work.md) supplies research attribution.

## Phase I — Background/preliminaries: M01–M13

### M01 — An unknown pure target and a mixed specimen

- **Central question:** What information about a qubit is retained when its state is mixed?
- **Understanding target:** A density operator describes the physical specimen, while the unknown pure target labels the direction against which performance is judged. The same density operator can have different ensemble descriptions without changing measurement predictions.
- **Dependencies and story role:** No earlier milestone. This introduces the individual physical object before several copies or a processing rule appear.
- **Conceptual connection:** Density operators separate the target of inference from the noisy state actually available.
- **Source pointers:** N&C §§2.4.1–2.4.2; [inputs and fidelity](../science/model-and-results.md#inputs-and-fidelity).

### M02 — Bloch length and the fidelity convention

- **Central question:** How do depolarization and fidelity become geometric quantities for one qubit?
- **Understanding target:** The noisy state has Bloch vector $`r\mathbf u`$ and target overlap $`F_0=(1+r)/2`$. The project uses overlap, the square of N&C's pure-target fidelity; pointwise ordering survives this change, but averaged quantities cannot be converted by squaring their averages.
- **Dependencies and story role:** M01. This fixes the baseline that every later gain is measured against.
- **Conceptual connection:** Bloch geometry turns purification into improved alignment with an unknown direction.
- **Source pointers:** N&C §§8.3.2, 8.3.4 and §9.2.2, especially Eq. (9.60); [inputs and fidelity](../science/model-and-results.md#inputs-and-fidelity).

### M03 — Several copies of the same unknown state

- **Central question:** What does independence mean when all inputs share an unknown direction?
- **Understanding target:** Conditional on fixed $`\mathbf u`$, the input is $`\rho_{\mathbf u}(r)^{\otimes n}`$. A prior average over the shared direction is generally not a tensor power of the single-copy prior average. A reserved copy is independent of other measurement records only conditional on that direction.
- **Dependencies and story role:** M01–M02. This moves from one specimen to the physical batch.
- **Conceptual connection:** Tensor products and latent classical information coexist without introducing independent target directions.
- **Source pointers:** N&C §§2.2.8 and 2.4.3; [inputs](../science/model-and-results.md#inputs-and-fidelity) and [fifth-copy operation](../science/constructions.md#deterministic-five-copy-operation).

### M04 — A Pauli measurement and its record

- **Central question:** What physical information is obtained by measuring one Pauli axis?
- **Understanding target:** A signed Pauli eigenprojector specifies both an outcome probability and the corresponding measured state. A choice of axis and a string of signs are classical records; recording, forgetting, or accepting a record produces different descriptions of the same instrument.
- **Dependencies and story role:** M01–M03. This introduces the elementary operation used by the attaining protocol.
- **Conceptual connection:** The Born rule connects a Bloch component to a usable directional signal.
- **Source pointers:** N&C §§2.2.3, 2.2.5 and 4.4; [accepted four-copy operation](../science/constructions.md#the-accepted-four-copy-operation).

### M05 — Conditional outputs and weighted scores

- **Central question:** How is the output state defined when only some measurement records are accepted?
- **Understanding target:** Accepted unnormalized branch states are summed and then divided by their total probability. Classical random choices must be included in that sum. The fidelity of the resulting state is an arithmetic average of overlaps weighted by accepted probabilities, not an equal average over records or root fidelities.
- **Dependencies and story role:** M02 and M04. This establishes the operational meaning of a conditional gain.
- **Conceptual connection:** Conditioning changes the ensemble weights while preserving linearity before normalization.
- **Source pointers:** N&C §§2.4.1, 8.2.3 and 9.2.2; [inputs and fidelity](../science/model-and-results.md#inputs-and-fidelity) and [universal averaging](../science/interpretation.md#the-role-of-universal-averaging).

### M06 — Accepted maps and channels

- **Central question:** Which mathematical constraints make an accepted operation physically possible?
- **Understanding target:** A completely positive map has Kraus operators; the inequality on their summed effects makes it trace nonincreasing. Its output trace is success probability. Equality makes the map trace preserving and includes all outcomes of a complete physical operation.
- **Dependencies and story role:** M03–M05. This packages a collection of branches into one linear object.
- **Conceptual connection:** A heralded map and a deterministic channel share complete positivity but differ in their normalization constraint.
- **Source pointers:** N&C §§8.2.3–8.2.4, Theorem 8.1; [allowed processing](../science/model-and-results.md#allowed-processing-and-the-comparison-cone).

### M07 — A map represented by a bipartite operator

- **Central question:** How can the action of an entire operation be encoded in a positive operator?
- **Understanding target:** The input-first Choi operator reconstructs the map through an input transpose. Its output partial trace is bounded by the input identity, with equality for a channel. A nonzero accepted map is normalized by $`\mathrm{tr}J`$, which need not equal the input dimension. In the Pauli expansion, $`Y^T=-Y`$ fixes a consequential sign.
- **Dependencies and story role:** M06. This prepares the representation used by both converses.
- **Conceptual connection:** Complete positivity becomes ordinary operator positivity on a larger space.
- **Source pointers:** N&C §8.2.4, Eqs. (8.56)–(8.65); [Choi convention and free class](../science/heralded-converse.md#choi-convention-and-the-free-class).

### M08 — Stabilizer states and constrained Pauli correlations

- **Central question:** Why are Pauli expectation values unusually rigid in a pure stabilizer state?
- **Understanding target:** Commuting Pauli generators specify the state. Each Pauli expectation is zero or a signed unit value, and anticommuting observables cannot both be stabilizers. Convex mixtures relax individual values while preserving linear inequalities established for pure stabilizer states.
- **Dependencies and story role:** M04. This supplies the local algebra behind the correlation bounds.
- **Conceptual connection:** Commutation translates a state restriction into constraints on measurable correlations.
- **Source pointers:** N&C §§2.1.9 and 10.5.1; [stabilizer correlation bound](../science/heralded-converse.md#the-stabilizer-correlation-bound).

### M09 — Stabilizer processing as an instrument

- **Central question:** Which measurement and preparation procedures stay within the allowed resource class?
- **Understanding target:** Clifford gates, stabilizer ancillas, Pauli measurements, classical randomness, conditional operations, and discarding implement stabilizer instruments. An accepted branch can lose trace without requiring a nonstabilizer resource. Measurement-and-preparation protocols form a concrete part of this class.
- **Dependencies and story role:** M06 and M08. This connects the state restriction to implementable processing.
- **Conceptual connection:** Closure under physical operations makes a resource restriction usable for both constructions and bounds.
- **Source pointers:** N&C §§10.5.1–10.5.3; [allowed processing](../science/model-and-results.md#allowed-processing-and-the-comparison-cone) and [accepted operation](../science/constructions.md#the-accepted-four-copy-operation).

### M10 — A pure Bell marginal forces factorization

- **Central question:** Why can a maximally correlated input-output pair prevent correlations with the remaining inputs?
- **Understanding target:** A pure bipartite marginal factors from the rest of the system. For a stabilizer state, two distinct nonzero correlations among $`X_iX_o`$, $`Y_iY_o`$, and $`Z_iZ_o`$ on the same pair fix a Bell state there, leaving its output uncorrelated with the other inputs. This is a structural constraint, not a numerical coincidence.
- **Dependencies and story role:** M03 and M08. This connects local correlation data to the global state.
- **Conceptual connection:** Reduced-state purity converts a pairwise statement into a restriction on many-body correlations.
- **Source pointers:** N&C §§2.4.3, 2.5 and 10.5.1; [Bell-pair case of the correlation bound](../science/heralded-converse.md#the-stabilizer-correlation-bound).

### M11 — The broader class used for the converse

- **Central question:** Why prove an upper bound for more maps than the construction needs?
- **Understanding target:** Stabilizer Choi operators form a convex cone. Its Bell-pair characterization gives completely stabilizer-preserving maps in the project's subnormalized setting. Ordinary stabilizer instruments lie in this class, but the argument does not assume every cone map has an ordinary stabilizer implementation.
- **Dependencies and story role:** M07, M09 and M10. This fixes the global comparison class before any impossibility claim.
- **Conceptual connection:** Convexity and ancillary systems turn a physical restriction into a stronger, tractable converse statement.
- **Source pointers:** N&C §§8.2.4 and 10.5.1 for foundations; the [Choi-cone argument](../science/heralded-converse.md#choi-convention-and-the-free-class) supplies the project-specific formulation, and [related work](../references/related-work.md#completely-stabilizer-preserving-channels) gives its research attribution.

### M12 — Haar averaging without losing the success weights

- **Central question:** How can an average over unknown directions constrain a guarantee for every direction?
- **Understanding target:** The Haar score divides integrated unnormalized overlap by integrated success. Odd spherical moments vanish, and second and fourth moments reduce the score to a few correlation coefficients. Pointwise positive gain implies positive accepted-data average gain; the reverse implication does not hold.
- **Dependencies and story role:** M02, M03, M05 and M06. This connects local experiments to a universal comparison.
- **Conceptual connection:** Rotational averaging simplifies the objective without requiring the operation itself to be rotation covariant.
- **Source pointers:** N&C §§2.4.1 and 8.3.2 for ensembles and geometry; [exact sphere moments](../science/heralded-converse.md#exact-three-copy-haar-expansion) and [universal averaging](../science/interpretation.md#the-role-of-universal-averaging) supply the local derivation.

### M13 — The complete operational question

- **Central question:** What precisely must an onset theorem quantify over?
- **Understanding target:** The question fixes the unknown-direction input model, overlap benchmark, allowable processing, copy budget, and success criterion. A map can depend on the known noise strength but cannot depend on the unknown direction. An onset identifies the first copy count allowing pointwise gain somewhere in the noisy-input domain; it does not assert gain at every noise strength.
- **Dependencies and story role:** M01–M12. This integrates the background into the single problem addressed by the research phase.
- **Conceptual connection:** Physical assumptions and mathematical quantifiers together determine what a construction and converse must establish.
- **Source pointers:** N&C §§8.2.4, 9.2.2 and 10.5.1–10.5.3; [main theorem](../science/model-and-results.md#main-theorem) and [scope](../science/model-and-results.md#scope-of-the-threshold).

## Phase II — Narrative/innovation: M14–M30

### M14 — The four-copy unanimity mechanism

- **Central question:** Which accepted records carry enough directional information to improve a weak signal?
- **Understanding target:** A uniformly chosen Pauli axis is measured on all four inputs. The protocol accepts only unanimous signs and returns the corresponding eigenstate. Its six Kraus operators define a physical stabilizer operation. The fixed-axis unanimity filter is inherited from estimation with abstention; the project makes its three-axis pointwise use explicit.
- **Dependencies and story role:** M04–M09 and M13. This starts the research phase with its concrete local mechanism.
- **Conceptual connection:** Selection on repeated measurement records amplifies useful information about an unknown direction.
- **Source pointers:** N&C §§2.2.5, 8.2.3 and 10.5.3; [accepted operation](../science/constructions.md#the-accepted-four-copy-operation) and [attribution](../references/related-work.md#estimation-with-abstention-the-inherited-construction).

### M15 — Exact success and conditional fidelity

- **Central question:** How does one compute the accepted output without mistaking branch scores for the protocol's score?
- **Understanding target:** Unanimous-event probabilities determine both the accepted trace and the unnormalized overlap. Their ratio gives the conditional fidelity. After averaging the three Pauli axes, the direction enters only through $`S_4=\sum_a u_a^4`$, while success remains direction dependent.
- **Dependencies and story role:** M02, M03, M05 and M14. This turns the physical mechanism into an exact expression.
- **Conceptual connection:** The conditional map keeps its linear branch structure until the final normalization.
- **Source pointers:** N&C §§2.2.3 and 8.2.3; [exact conditional gain](../science/constructions.md#exact-conditional-gain-for-every-direction).

### M16 — The worst direction and the pointwise interval

- **Central question:** Which target direction limits the four-copy guarantee?
- **Understanding target:** The bounds $`1/3\le S_4\le1`$ and monotonicity of the conditional fidelity make body diagonals the worst directions. Their gain is strictly positive for $`0\lt r\lt r_*`$, where $`r_* = \sqrt{-7+2\sqrt{13}}`$. This boundary belongs to the displayed construction, not to an optimization over all allowed maps.
- **Dependencies and story role:** M15. This upgrades a direction-dependent expression to a universal guarantee.
- **Conceptual connection:** A small geometric invariant controls the worst-case performance of a physical instrument.
- **Source pointers:** N&C §8.3.2 for qubit geometry; [pointwise bound](../science/constructions.md#exact-conditional-gain-for-every-direction) and [scope](../science/model-and-results.md#scope-of-the-threshold).

### M17 — The average score and an exact witness

- **Central question:** Why is a favorable Haar average weaker than improvement for every direction?
- **Understanding target:** Integrating the unnormalized quantities gives $`\mathbb E[S_4]=3/5`$ and the exact accepted-data Haar formula. Its positive-gain interval is larger than the pointwise interval. At $`r=1/3`$, the raw overlap is $`2/3`$, the worst-direction conditional overlap is $`307/446`$, and the Haar score is $`43/62`$; these are different, compatible quantities.
- **Dependencies and story role:** M12, M15 and M16. This connects the constructive guarantee to the objective used in the converse.
- **Conceptual connection:** Average and worst-case performance require different mathematical evidence.
- **Source pointers:** N&C §§2.4.1 and 9.2.2; [Haar score and exact example](../science/constructions.md#haar-score-and-an-exact-example).

### M18 — Any prescribed average success below one

- **Central question:** Can the four-copy gain survive a specified acceptance probability?
- **Understanding target:** Below the filter's mean success $`p_0`$, an independent acceptance coin reduces success without changing conditional fidelity. Above $`p_0`$, mixing the filter with return-one-input reaches any prescribed $`0\lt\overline p\lt1`$. In the pointwise interval, the gain remains strictly positive because the filter retains positive weight; the gain tends to zero as average success tends to one.
- **Dependencies and story role:** M06 and M15–M17. This makes the construction meet a continuous operational constraint.
- **Conceptual connection:** Convex mixing changes yield while its weighted overlap tracks the retained advantage.
- **Source pointers:** N&C §§2.4.1 and 8.2.3; [prescribing average success](../science/constructions.md#prescribing-average-success).

### M19 — Three-copy averaging becomes an affine sign problem

- **Central question:** How does the heralded converse reduce an arbitrary accepted map to a few numbers?
- **Understanding target:** The Choi expansion and sphere moments express success and overlap through $`A,B,C`$. After subtracting the raw benchmark, the gap has a positive factor times an affine polynomial in $`r^2`$. Full rank of noisy inputs makes the denominator positive for every nonzero accepted map in the open noisy domain.
- **Dependencies and story role:** M07, M11–M13. This begins the converse with its algebraic reduction, independent of the particular construction.
- **Conceptual connection:** Symmetry of the objective simplifies a completely general map without imposing symmetry on that map.
- **Source pointers:** N&C §8.2.4; [three-copy Haar expansion](../science/heralded-converse.md#exact-three-copy-haar-expansion).

### M20 — The three-copy output-correlation budget

- **Central question:** Why can the three inputs supply at most three signed Pauli correlations with the output?
- **Understanding target:** For a pure stabilizer Choi state, either a pair carries enough correlations to force a Bell factor, or each input contributes at most one relevant correlation. Both cases give $`B\le3`$, and convexity extends the bound to stabilizer mixtures. This controls the constant endpoint of the affine polynomial.
- **Dependencies and story role:** M08, M10 and M19. This supplies the resource-specific part of the heralded converse.
- **Conceptual connection:** Local Pauli rigidity and global factorization jointly limit how information can reach one output.
- **Source pointers:** N&C §§2.5 and 10.5.1 for the prerequisites; [stabilizer correlation bound](../science/heralded-converse.md#the-stabilizer-correlation-bound) supplies the exact inequality.

### M21 — The endpoint with possibly zero acceptance

- **Central question:** How can the pure-state endpoint be used when its conditional fidelity may be undefined?
- **Understanding target:** A positive integrated error operator bounds the unnormalized endpoint directly, so no division by a possibly zero success occurs. Together with $`B\le3`$, it makes both endpoints of the affine polynomial nonpositive. Interpolation holds the chosen map fixed; universality over maps still permits a different map to be selected at each noise strength.
- **Dependencies and story role:** M19–M20. This completes the sign argument without an endpoint loophole.
- **Conceptual connection:** Positivity replaces a problematic normalized quantity with a well-defined linear witness.
- **Source pointers:** N&C §8.2.4 for positivity of maps; [pure-state endpoint](../science/heralded-converse.md#the-pure-state-endpoint-including-zero-success).

### M22 — The sharp heralded minimum

- **Central question:** How do the three-copy upper bound and four-copy construction become an exact threshold?
- **Understanding target:** Padding with unused inputs extends the converse to one and two copies. Returning one input with an independent acceptance coin attains the raw benchmark at every prescribed positive success up to one. Since pointwise gain would imply a positive weighted Haar gain, the converse rules it out below four; M16–M18 attain it with four for every prescribed average success strictly below one in the stated interval.
- **Dependencies and story role:** M13, M16, M18 and M21. This integrates the heralded part of the research.
- **Conceptual connection:** A bound for an easier averaged objective can establish sharpness for a stronger universal task.
- **Source pointers:** N&C §§8.2.3–8.2.4; [fewer copies and equality](../science/heralded-converse.md#fewer-copies-and-equality-at-every-success-probability) and [four-copy onset](../science/heralded-converse.md#statewise-consequence-and-the-four-copy-onset).

### M23 — What trace preservation adds to the Choi state

- **Central question:** Which extra restriction distinguishes a deterministic four-copy map from an accepted one?
- **Understanding target:** A trace-preserving map has normalized Choi input marginal equal to the maximally mixed state. Every nonidentity input-only Pauli expectation therefore vanishes. This is stronger than the trace bound for a heralded map and cannot be inserted into the four-copy accepted problem.
- **Dependencies and story role:** M06, M07 and M11. This begins the deterministic argument with the extra physical constraint that makes it possible.
- **Conceptual connection:** Normalization of an operation becomes a family of correlation identities.
- **Source pointers:** N&C §§2.4.3 and 8.2.4; [deterministic Choi convention](../science/deterministic-converse.md#choi-convention).

### M24 — A four-body correction to the correlation bound

- **Central question:** How does the four-input case account for an additional possible output correlation?
- **Understanding target:** On five-qubit stabilizer states, the inequality is $`B\le3+D`$, where $`D`$ sums three four-input Pauli correlations. Bell-factor and common-axis cases establish this bound; trace preservation then forces $`D=0`$. The inequality is an expectation bound on the stabilizer set, not an operator inequality valid on all states.
- **Dependencies and story role:** M08, M10, M20 and M23. This supplies the new correlation structure needed for four inputs.
- **Conceptual connection:** A many-body correction records the exceptional correlation pattern that the deterministic constraint removes.
- **Source pointers:** N&C §§2.1.9 and 10.5.1 for Pauli algebra; [five-qubit stabilizer inequality](../science/deterministic-converse.md#a-five-qubit-stabilizer-inequality) supplies the exact result.

### M25 — The deterministic four-copy upper bound

- **Central question:** Why does the additional trace constraint rule out deterministic improvement with four inputs?
- **Understanding target:** Haar expansion gives $`F^{\mathrm H}=1/2+Br/6+Cr^3/30`$. After subtracting $`F_0`$ and dividing by positive $`r`$, the remaining expression is affine in $`r^2`$. The bound $`B\le3`$ fixes one endpoint, and physical output fidelity at the pure endpoint fixes the other. Unused-copy padding covers all smaller deterministic budgets.
- **Dependencies and story role:** M19, M21 and M23–M24. This completes the second converse while showing what it shares with the first.
- **Conceptual connection:** The same interpolation strategy uses a different resource constraint and a simpler normalized endpoint.
- **Source pointers:** N&C §§8.2.4 and 9.2.2; [four-copy coefficients](../science/deterministic-converse.md#exact-four-copy-haar-coefficients) and [endpoint interpolation](../science/deterministic-converse.md#endpoint-interpolation-and-equality).

### M26 — A fifth copy completes the physical operation

- **Central question:** How can rejected four-copy records be supplied with an output without erasing the gain?
- **Understanding target:** An untouched fifth copy is returned on failure, while accepted runs use the filter's output. Conditional independence at fixed target makes the failure contribution exactly the raw fidelity. The complete map is trace preserving, and its pointwise gain is $`p_{\mathbf u}(F_{4,\mathbf u}-F_0)`$. Determinism means an output on every record, not improvement on every individual record.
- **Dependencies and story role:** M03, M06, M16 and M25. This matches the deterministic lower bound with a physical construction.
- **Conceptual connection:** Completing an instrument with an independent fallback converts conditional advantage into unconditional advantage.
- **Source pointers:** N&C §§2.2.8 and 8.2.3; [five-copy operation](../science/constructions.md#deterministic-five-copy-operation).

### M27 — Batch size, delivered outputs, and physical cost

- **Central question:** What resource is counted by a four-versus-five threshold?
- **Understanding target:** Four inputs are consumed per attempt by the bare filter. Fresh repeated attempts at fixed direction have expected cost $`4/p_{\mathbf u}\le32`$, with no finite worst-case bound. The deterministic construction counts five inputs per fixed batch, including the reserved copy on successful runs. Modified success probabilities have their own repeat costs.
- **Dependencies and story role:** M18, M22 and M26. This interprets the attained copy counts without conflating them with average consumption.
- **Conceptual connection:** A heralded batch threshold and a cost per delivered output are distinct operational quantities.
- **Source pointers:** N&C §8.2.3 for outcome probabilities; [physical budget](../science/interpretation.md#postselection-and-the-physical-budget) supplies this accounting.

### M28 — The probability-one boundary

- **Central question:** Why does prescribing only average success not evade the deterministic bound at one?
- **Understanding target:** For $`r\lt1`$, the averaged input is positive definite. A positive rejection effect with zero expectation in that state must vanish, so average success one forces trace preservation. Four copies suffice at each prescribed $`0\lt\overline p\lt1`$ in the pointwise interval, while five are necessary and sufficient at $`\overline p=1`$ there; the attainable four-copy gain shrinks to zero at the endpoint.
- **Dependencies and story role:** M06, M18, M22–M26. This joins the heralded and deterministic conclusions at their common boundary.
- **Conceptual connection:** Full rank converts an averaged probability condition into an operator identity.
- **Source pointers:** N&C §§2.4.2 and 8.2.4; [average success one](../science/model-and-results.md#why-average-success-one-is-deterministic) and [prescribed success](../science/constructions.md#prescribing-average-success).

### M29 — What is purified, and which ingredients are inherited?

- **Central question:** What physical and scientific claim does the sharp threshold add to the unanimity mechanism?
- **Understanding target:** In the proved interval, inputs and accepted outputs can all be stabilizer mixtures; improvement concerns fidelity to an unknown direction, not creation of a fixed nonstabilizer resource. The unanimity filter and channel Choi characterization have prior sources. The sharp result relies on the three-copy accepted-map and four-copy deterministic converses, which constrain coherent maps beyond measurement-and-preparation strategies.
- **Dependencies and story role:** M09, M11, M14, M22 and M25–M28. This places the completed mechanism and bounds in their physical and scientific setting.
- **Conceptual connection:** State estimation, resource restrictions, and universal impossibility bounds answer different parts of the same task.
- **Source pointers:** N&C §§8.3.2 and 10.5.1; [directional information](../science/interpretation.md#stabilizer-resources-and-directional-information) and [contribution and conventions](../references/related-work.md#contribution-and-conventions).

### M30 — The complete threshold and its exact scope

- **Central question:** Which claims follow when construction, converse, success constraint, and resource accounting are combined?
- **Understanding target:** The exact onset is four heralded inputs and five deterministic inputs. The converse bounds cover every $`0\lt r\lt1`$ in the stated Choi class; the ordinary stabilizer constructions give pointwise gain for $`0\lt r\lt r_*`$. Prescribed success below one, the probability-one endpoint, accepted-data weighting, and fixed batch costs retain their distinct meanings. Neither an optimal fidelity-yield frontier, a construction valid at every noise strength, nor iterative convergence to pure outputs is established.
- **Dependencies and story role:** M13 and M14–M29. This is the global synthesis of the research phase.
- **Conceptual connection:** Sharpness comes from matching broad upper bounds with implementable operations at the same operational threshold.
- **Source pointers:** N&C §§8.2.4, 9.2.2 and 10.5.1–10.5.3 for the combined foundations; [main theorem and scope](../science/model-and-results.md#main-theorem), [what closes the theorem](../science/interpretation.md#what-closes-the-theorem), and [verification boundaries](../verification/README.md#what-each-check-establishes).
