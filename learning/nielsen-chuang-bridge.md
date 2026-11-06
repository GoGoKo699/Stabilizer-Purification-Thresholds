# From Nielsen–Chuang to the copy threshold

An unknown source prepares qubits with the same pure Bloch direction. Independent
depolarization weakens each copy's directional signal. A protocol receives several
copies and returns one qubit that should approximate the original direction more
accurately. It may either announce failure or be required to return an output on
every run. This distinction produces the project's four-copy heralded threshold
and five-copy deterministic threshold.

The useful output must approximate the unknown target. A pure measurement outcome
alone does not ensure that: its direction can be poorly aligned with the source.
The connection between states, measurement records, conditional maps and target
overlap is therefore central to the result.

## The selected source and its role

The educational anchor is **Michael A. Nielsen and Isaac L. Chuang, _Quantum
Computation and Quantum Information_, 10th Anniversary Edition (2010), Cambridge
University Press**, [DOI: 10.1017/CBO9780511976667](https://doi.org/10.1017/CBO9780511976667).
The [publisher's contents](https://assets.cambridge.org/97811070/02173/toc/9781107002173_toc.pdf)
give the following locations; page numbers are printed page numbers in that edition.

| Source location | Foundation | Connection developed here |
|---|---|---|
| §8.2.4, p. 366 | Completely positive operations and their operator-sum representation | Accepted maps, trace bounds, and the map-state representation |
| §8.3.4, p. 378 | Depolarization | Bloch polarization and the noisy input family |
| §9.2.2, p. 409 | Root fidelity | The project's overlap convention and its averages |
| §10.5.1, p. 454 | Stabilizer groups and states | Discrete Pauli expectations |
| §10.5.2, p. 459 | Unitary evolution in the stabilizer formalism | Clifford processing |
| §10.5.3, p. 463 | Stabilizer measurements | Pauli measurement and conditional branches |
| §10.5.4, p. 464 | Classical simulation of stabilizer circuits | The restricted circuit framework |

These sections supply the foundations. The accepted-map stabilizer cone, its
correlation inequalities, and the four-versus-five threshold are developed in the
project. The links below connect the source to those additional steps without
repeating the full [heralded](../science/heralded-converse.md) and
[deterministic](../science/deterministic-converse.md) proofs.

## 1. Bloch geometry fixes the target and the benchmark

Write the pure target and its noisy copy as

```math
\psi_{\mathbf u}=\frac{I+\mathbf u\cdot\boldsymbol\sigma}{2},
\qquad
\rho_{\mathbf u}(r)=r\psi_{\mathbf u}+(1-r)\frac I2
=\frac{I+r\mathbf u\cdot\boldsymbol\sigma}{2},
\qquad |\mathbf u|=1.
```

The unit vector $`\mathbf u`$ specifies direction; $`r`$ specifies the length of the
noisy Bloch vector. Throughout the task, $`0\lt r\lt1`$. The target is the principal
eigenstate of the input, whose eigenvalues are $`(1+r)/2`$ and $`(1-r)/2`$.
The parameter translation to the project's depolarizing replacement channel is

```math
\mathcal D_\delta(\rho)=(1-\delta)\rho+\delta\frac I2,
\qquad \delta=1-r.
```

This is the connection to §8.3.4. Matching the channel formula fixes the meaning
of the noise parameter: small $`r`$ means strong depolarization. The copies are
independent conditional on the fixed unknown direction, so the joint input is
$`\rho_{\mathbf u}(r)^{\otimes n}`$.

The target enters the mathematical score even though the protocol does not know
it. A single map must work for every direction. Its design may use the fixed
polarization $`r`$, but may not use $`\mathbf u`$. These quantifiers are specified
in [the model](../science/model-and-results.md#inputs-and-fidelity).

### Translating the book's fidelity

Nielsen–Chuang §9.2.2 uses root fidelity, with the general definition in Eq. (9.53)
and its pure-state specialization in Eq. (9.60):

```math
F_{\mathrm{NC}}(\rho,\omega)
=\mathrm{tr}\sqrt{\sqrt\rho\,\omega\sqrt\rho},
\qquad
F_{\mathrm{NC}}(\psi_{\mathbf u},\omega)
=\sqrt{\mathrm{tr}(\psi_{\mathbf u}\omega)}.
```

The project uses the squared quantity, called **overlap fidelity** here:

```math
F(\psi_{\mathbf u},\omega)
=F_{\mathrm{NC}}(\psi_{\mathbf u},\omega)^2
=\mathrm{tr}(\psi_{\mathbf u}\omega).
```

Its raw benchmark is consequently

```math
F_0(r)=\mathrm{tr}\bigl[\psi_{\mathbf u}\rho_{\mathbf u}(r)\bigr]
=\frac{1+r}{2}.
```

For one fixed pair of normalized states, strict improvement is equivalent under
squaring. Averaging changes the issue: an average of squares is generally not the
square of an average. The overlap convention must therefore remain fixed when
measurement outcomes or target directions are averaged. Its linear dependence on
the output density operator will also make the converse manageable.

## 2. Success belongs inside an unnormalized operation

The operator-sum viewpoint of §8.2.4 distinguishes an operation from its
normalized conditional output. Let $`M_k`$ be Kraus operators from the joint input
space to the output qubit. For a collection $`\mathcal A`$ of accepted branches,

```math
\mathcal E(X)=\sum_{k\in\mathcal A}M_kXM_k^\dagger,
\qquad
\sum_{k\in\mathcal A}M_k^\dagger M_k\le I.
```

The output $`\mathcal E(X)`$ retains its probability weight. On the input family,
define

```math
\widetilde\rho_{\mathbf u}
=\mathcal E\bigl(\rho_{\mathbf u}(r)^{\otimes n}\bigr),
\qquad
p_{\mathbf u}=\mathrm{tr}\widetilde\rho_{\mathbf u},
\qquad
\rho_{\mathbf u}^{\mathrm{acc}}
=\frac{\widetilde\rho_{\mathbf u}}{p_{\mathbf u}}.
```

The trace is success probability; division produces the state conditioned on
success. If every outcome is included, the Kraus completeness relation is an
equality and the operation is trace preserving.

For a nonzero accepted map, the acceptance effect
$`Q_{\mathrm{acc}}=\sum_{k\in\mathcal A}M_k^\dagger M_k`$ is positive and nonzero.
Its expectation in a positive-definite input is strictly positive. Because both
input eigenvalues are positive for $`r\lt1`$, this guarantees
$`p_{\mathbf u}\gt0`$ at every direction in the noisy-input domain. Conditional
normalization is therefore legitimate there.

The physical map $`X\mapsto\mathcal E(X)`$ is linear. Two later operations produce
the nonlinear expressions seen in the project: restricting its argument to
$`X=\rho_{\mathbf u}(r)^{\otimes n}`$ produces powers of $`r`$, and conditioning
divides by a state-dependent trace. Neither changes the linearity of the
underlying operation on its joint input.

Classical random choices also belong in this description. A choice made with
probability $`w`$ multiplies that branch's Kraus operators by $`\sqrt w`$. Thus the
random Pauli axis and all accepted signs are included in one accepted map. The
[construction page](../science/constructions.md#the-accepted-four-copy-operation)
gives its explicit Kraus operators.

### Why normalization follows averaging

There are two distinct sums. First fix $`\mathbf u`$ and combine accepted
measurement records. If record $`k`$ has probability $`p_{\mathbf u,k}`$ and
conditional overlap $`F_{\mathbf u,k}`$, the accepted overlap is

```math
F_{\mathcal E,\mathbf u}
=\frac{\sum_{k\in\mathcal A}p_{\mathbf u,k}F_{\mathbf u,k}}
{\sum_{k\in\mathcal A}p_{\mathbf u,k}}.
```

Giving each normalized branch equal weight would describe a different experiment.
Branches occur according to their Born probabilities.

Next consider a uniform distribution of possible directions, with normalized
measure $`d\mu(\mathbf u)`$. Accepted data have the reweighted distribution

```math
d\mu_{\mathrm{acc}}(\mathbf u)
=\frac{p_{\mathbf u}}{\overline p}\,d\mu(\mathbf u),
\qquad
\overline p=\int p_{\mathbf u}\,d\mu(\mathbf u).
```

The project's conditional Haar score is therefore

```math
F_{\mathcal E}^{\mathrm H}
=\int F_{\mathcal E,\mathbf u}\,d\mu_{\mathrm{acc}}(\mathbf u)
=\frac{\int\mathrm{tr}(\psi_{\mathbf u}\widetilde\rho_{\mathbf u})
\,d\mu(\mathbf u)}{\int p_{\mathbf u}\,d\mu(\mathbf u)}.
```

This formula explains why the unnormalized accepted map is retained so long.
Both its numerator and its denominator can be evaluated before division. It also
explains the direction of the converse: because $`F_0(r)`$ is independent of
$`\mathbf u`$, strict improvement at every direction would improve this
success-weighted score. An upper bound on the score can rule out the stronger
pointwise task. A positive Haar gain alone does not establish a pointwise gain.

## 3. One batch at polarization one third

Take $`r=1/3`$, so an unprocessed input has overlap $`F_0=2/3`$. Consider a
body-diagonal direction,

```math
\mathbf u=\frac{(1,1,1)}{\sqrt3}.
```

The four-copy protocol chooses a Pauli axis uniformly and accepts only unanimous
signs. In this direction every axis has the same single-copy sign probabilities

```math
q_\pm=\frac{1\pm1/(3\sqrt3)}2.
```

Independence makes the two unanimous events have probabilities $`q_+^4`$ and
$`q_-^4`$. The three possible axes give the same total in this example, so

```math
p_{\mathrm{diag}}=q_+^4+q_-^4=\frac{223}{1458}.
```

Retaining one measured copy on success yields the overlap listed below. The
general formulas and their directional bound are in the
[exact construction](../science/constructions.md#exact-conditional-gain-for-every-direction).

| Evaluation at $`r=1/3`$ | Success probability | Output overlap |
|---|---:|---:|
| Four-copy filter, body-diagonal direction | $`223/1458`$ | $`307/446`$ |
| Four-copy filter, accepted-data Haar score | $`62/405`$ | $`43/62`$ |
| Five-copy channel, body-diagonal direction | $`1`$ | $`2/3+29/8748`$ |

The first row is the worst-direction case for this filter. The second uses its
natural Haar-average success, without any additional thinning or mixing. Its
larger fidelity is an accepted-data average, not the minimum over directions.
Both four-copy overlaps exceed $`2/3`$; the
[rational example](../science/constructions.md#haar-score-and-an-exact-example)
records the other exact values.

The third row uses a separate untouched fifth input when the first four are
rejected. Conditional on a fixed direction, rejection does not change that
independent fifth state. Its fidelity gain is therefore the accepted four-copy
gain multiplied by the four-copy success probability:

```math
\frac{223}{1458}\left(\frac{307}{446}-\frac23\right)
=\frac{29}{8748}.
```

Resource counts distinguish these rows. A four-copy batch may fail. Repeating
fresh batches from the same fixed source until acceptance has expected input cost
$`4/p_{\mathbf u}`$; in the displayed direction this is
$`5832/223\approx26.15`$ copies. It is not a fixed upper bound on a particular
run. Averaging that cost over possible fixed sources would average
$`4/p_{\mathbf u}`$, rather than replace $`p_{\mathbf u}`$ by $`\overline p`$.
The five-copy construction always returns a qubit after one batch of five, with
a smaller gain. The threshold compares these output requirements, while any
comparison at equal final fidelity needs its own resource calculation. See
[physical budgets](../science/interpretation.md#postselection-and-the-physical-budget).

## 4. From a quantum operation to a Choi operator

The proof of Theorem 8.1 in §8.2.4 uses a maximally entangled input to represent a
map by an operator; Eqs. (8.56)–(8.65) are the relevant map-state steps. The project
fixes its own normalization and tensor order explicitly. For $`n`$ inputs, write

```math
|\Omega_n\rangle=\sum_{x\in\{0,1\}^n}|x\rangle_A|x\rangle_{A'},
\qquad
J_{\mathcal E}=(\mathrm{id}_A\otimes\mathcal E)
\bigl(|\Omega_n\rangle\langle\Omega_n|\bigr).
```

Here $`A`$ is an input reference, $`A'`$ is the copy on which the map acts, and the
output is called $`o`$. The final ordering of $`J_{\mathcal E}`$ is reference
first, output last. The vector $`|\Omega_n\rangle`$ is unnormalized. For an input
operator $`X`$ and output observable $`O`$,

```math
\mathrm{tr}\bigl[O\mathcal E(X)\bigr]
=\mathrm{tr}\bigl[J_{\mathcal E}(X^T\otimes O)\bigr].
```

This identity turns a statement about every possible circuit into a statement
about one positive operator. Complete positivity and trace nonincrease become

```math
J_{\mathcal E}\ge0,
\qquad
\mathrm{tr}_oJ_{\mathcal E}\le I_A.
```

The Bell-pair input is a mathematical representation of the operation. The
physical purifier's input budget is the noisy copies specified in its
construction.

The distinction between three related operators matters:

- $`J_{\mathcal E}`$ is the unnormalized Choi operator.
- $`J_{\mathcal E}/2^n`$ is the actual output from normalized Bell-pair input;
  its trace may be less than one for an accepted map.
- $`j=J_{\mathcal E}/\tau`$, with $`\tau=\mathrm{tr}J_{\mathcal E}`$, is the
  normalized state used for the proof's expectation values.

For a channel, $`\tau=2^n`$ and
$`\mathrm{tr}_o j=I_A/2^n`$. For a heralded operation, that maximally mixed input
marginal is not imposed. This difference will supply the extra deterministic
restriction in the four-input converse.

### The transpose and the stabilizer cone

The transpose in the reconstruction identity is in the computational basis. It
acts on the Pauli matrices as

```math
X^T=X,\qquad Y^T=-Y,\qquad Z^T=Z.
```

Consequently, the input-output correlation sum appearing in the proof is

```math
B=\sum_{i=1}^n
\left\langle X_iX_o-Y_iY_o+Z_iZ_o\right\rangle_j.
```

The minus sign is fixed by the map representation. It is consistent with the
Bell state $`|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2`$, whose pair
correlations are $`+1,-1,+1`$ for $`XX,YY,ZZ`$ respectively.

The project adds a restriction to the positive-operator description:

```math
J_{\mathcal E}=\sum_k c_k|s_k\rangle\langle s_k|,
\qquad c_k\ge0,
```

where the $`|s_k\rangle`$ are pure stabilizer states on the input references and
output. It is a cone rather than a set of normalized states because changing the
success scale must be allowed. After dividing by $`\tau`$, $`j`$ is a convex
mixture of stabilizer projectors.

Ordinary stabilizer instruments satisfy this condition: feeding their input
halves of stabilizer Bell pairs produces such a mixture on acceptance. The
converse also holds in the sense of complete preservation of the subnormalized
stabilizer cone, using Bell projections to reconstruct the map. That statement
defines the larger comparison class; it does not assert an ordinary-circuit
implementation for every map with its specified success normalization. The
[Choi-cone argument](../science/heralded-converse.md#choi-convention-and-the-free-class)
makes the distinction precise.

This representation supplies a useful route to a universal lower bound. A linear
expectation inequality proved on pure stabilizer projectors also holds on their
mixtures. One need not enumerate every adaptive circuit that might be attempted.

## 5. Commutation turns circuit restrictions into correlation restrictions

Sections 10.5.1–10.5.3 supply the stabilizer language for this step. A pure
$`m`$-qubit stabilizer state is fixed by a maximal commuting Pauli group
$`\mathcal S`$. Its projector can be expressed as

```math
|s\rangle\langle s|=2^{-m}\sum_{g\in\mathcal S}g.
```

Pauli orthogonality then makes every Hermitian Pauli expectation either
$`0`$, $`+1`$ or $`-1`$. A nonzero value means that the state has a definite
eigenvalue for that Pauli. Anticommutation gives the other useful rule: if a
stabilizer $`g`$ anticommutes with $`P`$, then

```math
\langle P\rangle=\langle gPg\rangle=-\langle P\rangle=0.
```

The distinction between sharing one qubit and sharing two is decisive. The pair
operators $`X_iX_o`$ and $`Z_iZ_o`$ commute because their two local
anticommutations cancel. Fixing both eigenvalues selects a one-dimensional Bell
subspace on that input-output pair. A pure global state supported there factors
into that Bell state and the remaining inputs. The output's maximally mixed
single-qubit marginal then removes its Pauli correlations with those other
inputs.

By contrast, $`X_iX_o`$ and $`Z_kZ_o`$ with $`i\ne k`$ share only the output and
anticommute. They cannot both have definite eigenvalues in one state. These facts
limit how many perfect pair correlations can coexist. They are the mechanism
behind the three-input bound $`B\le3`$. The complete cases and their extension to
mixtures are in the
[stabilizer correlation lemma](../science/heralded-converse.md#the-stabilizer-correlation-bound).

The deterministic four-input proof needs one additional connection. Define the
input-only expectation

```math
D=\left\langle
X^{\otimes4}+Y^{\otimes4}+Z^{\otimes4}
\right\rangle_j.
```

The [five-qubit stabilizer inequality](../science/deterministic-converse.md#a-five-qubit-stabilizer-inequality)
is $`B\le3+D`$. The four-body term accounts for the extra aligned pair
correlations that four inputs can support. Trace preservation now matters: the
input marginal of $`j`$ is $`I/16`$, so every nonidentity input-only Pauli has zero
expectation and $`D=0`$. This again forces $`B\le3`$.

The textbook's stabilizer formalism explains why commutation and eigenvalues are
useful. The bounds $`B\le3`$ and $`B\le3+D`$ are the project-specific steps that
turn those facts into purification converses. Classical simulation of stabilizer
circuits, treated in §10.5.4, is not by itself a bound on their purification score.

## 6. Why two endpoints control the entire noise interval

Fix one allowed map. Its action on $`\rho_{\mathbf u}(r)^{\otimes n}`$ is a
polynomial in $`r`$ of degree at most $`n`$. Uniform direction averaging removes
odd coordinate moments, while the overlap with $`\psi_{\mathbf u}`$ can supply
one additional directional factor. Rotational symmetry also fixes
$`\int u_a u_b\,d\mu=\delta_{ab}/3`$. The fourth moments reduce to the three
possible pairings of four indices.

For three inputs, this leaves a success polynomial of degree two and an overlap
numerator of degree three. For four trace-preserving inputs, the input-only terms
are fixed by the channel normalization, leaving a fidelity polynomial with
linear and cubic terms. The
[three-input expansion](../science/heralded-converse.md#exact-three-copy-haar-expansion)
and [four-input expansion](../science/deterministic-converse.md#exact-four-copy-haar-coefficients)
give every coefficient.

The resulting gaps have the forms

```math
F_{\mathcal E}^{\mathrm H}(r)-F_0(r)
=\frac{r}{2d_3(r)}q_3(r^2)
\quad\text{for three accepted inputs},
```

```math
F_{\mathcal E}^{\mathrm H}(r)-F_0(r)
=\frac r2q_4(r^2)
\quad\text{for four trace-preserving inputs}.
```

Here $`d_3(r)=8\overline p/\tau\gt0`$ for $`r\lt1`$, and each $`q`$ is affine
in its argument. The remaining issue is its sign.

At the limiting point $`r=0`$, the inputs carry no direction information. The relevant endpoint for
the proof is more precise than that observation: it is the first-order gain
coefficient after division by $`r`$. The correlation bound $`B\le3`$ makes
$`q(0)\le0`$. The equality $`F^{\mathrm H}(0)=1/2`$ alone would not supply that
derivative bound.

At $`r=1`$, a normalized output cannot have overlap greater than one with a pure
target. A heralded map can, however, have zero success on pure inputs. Its proof
therefore uses the positive unnormalized operator

```math
W_3=\int(\psi_{\mathbf u}^{T})^{\otimes3}
\otimes(I-\psi_{\mathbf u})\,d\mu(\mathbf u)\ge0.
```

Its expectation gives $`q_3(1)\le0`$ without dividing by a possibly zero success.
For a channel, success remains one and the ordinary pure-state fidelity bound
gives $`q_4(1)\le0`$. The
[heralded endpoint argument](../science/heralded-converse.md#the-pure-state-endpoint-including-zero-success)
contains the exact relation between $`W_3`$ and the moment coefficients.

Affineness now joins the endpoint statements:

```math
q(s)=(1-s)q(0)+s q(1)\le0,
\qquad 0\le s\le1.
```

This is stronger than continuity: a general curved function could be positive
between two nonpositive endpoints. The low polynomial degree is what closes the
argument. The same map is held fixed when its endpoints are tested. Since the
bound holds for every map, the actual protocol may still be designed for a fixed
known noise level.

## 7. How the pieces meet at four and five

The accepted-map converse excludes any improvement in the success-weighted Haar
score with at most three inputs, and therefore excludes strict improvement for
every direction. Four-input trace-preserving maps obey the corresponding
deterministic bound. Returning an input attains equality in those bounds; an
independent acceptance coin attains it at any prescribed positive average success
for the heralded lower budgets.

The [four-copy instrument](../science/constructions.md) and its fifth-copy
fallback attain strict pointwise gain for

```math
0\lt r\lt r_*:=\sqrt{-7+2\sqrt{13}}.
```

Their conjunction with the converses gives an exact minimum of four copies with
heralding and five when every run returns an output, throughout this interval.
The claim concerns the onset of a positive gain. It supplies neither an optimal
fidelity curve nor a guarantee at every polarization. The
[main theorem](../science/model-and-results.md#main-theorem) is the canonical
statement of those quantifiers.

Prescribing success makes the boundary more precise. Below the filter's natural
Haar-average success, independent thinning discards some successful runs without
changing their conditional output. Above its natural success, mixing the filter
with a channel that returns one supplied input and discards the other three
raises the acceptance rate. The return-one branch contributes exactly the raw
fidelity, so the filter's positive unnormalized gain survives at every nonzero
mixing weight. These two operations give strict pointwise gain at every prescribed
average success $`0\lt p\lt1`$ for a fixed $`r`$ in the stated interval. The
[success-tuning construction](../science/constructions.md#prescribing-average-success)
gives the mixing probabilities.

Average success exactly one changes the constraint. The rejection effect is a
positive operator, while the averaged noisy input is positive definite. Zero
average rejection therefore forces the rejection effect itself to vanish, so
the accepted map is trace preserving. The four-input deterministic converse now
applies. This is why tuning success toward one does not produce a four-copy
channel with a strict gain at one; the fifth-copy fallback supplies that output
requirement. The [probability-one argument](../science/model-and-results.md#why-average-success-one-is-deterministic)
states the positivity step explicitly.

Research attribution is separate from this educational source: the fixed-axis
unanimity mechanism comes from Gendra et al. (2012), the proved two-copy no-go from
He et al. (2026), and the channel Choi characterization from Seddon and Campbell
(2019). Their roles and the project-specific additions are documented in
[related work](../references/related-work.md).

The [learning overview](README.md) and [understanding map](milestones.md) organize
these connections. The [scientific account](../science/README.md) provides the
full statements, constructions and proofs, and the
[verification guide](../verification/README.md) distinguishes executable checks
from the analytical guarantees.
