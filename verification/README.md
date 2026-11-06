# Reproduce the finite and algebraic checks

The verification scripts test the explicit quantum maps, exact moment coefficients and feasible Choi witnesses. The universal gain and the stabilizer-ray inequalities are proved in the [scientific account](../science/README.md); finite samples do not establish those claims by themselves.

The separate [hosted mathematics check](hosted/README.md) compares equations on actual GitHub pages with a pinned source revision and retains screenshots for visual review.

## Run

The recorded runs used Python 3.12.14, NumPy 2.3.5 and SymPy 1.14.0. From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/verify_constructions.py --output verification/construction_results.json
python verification/verify_converse_operator_coefficients.py
python verification/check_published_sdp_witness.py
```

The commands need no network access after dependencies are installed. They rewrite the corresponding JSON reports beside the scripts. All checks must pass; floating-point residuals may differ slightly across platforms.

## What each check establishes

| Script and report | Method | Scope |
|---|---|---|
| [verify_constructions.py](verify_constructions.py), [construction_results.json](construction_results.json) | Builds six accepted four-input Kraus operators and the complete 54-operator five-input channel. Checks effects, joint-input outputs, conditional gains, Haar quadrature and prescribed-success mixtures; also verifies exact symbolic identities and rational witnesses. | 336 direct joint-input cases and 630 prescribed-success cases in the default run, including polarizations on both sides of the displayed boundary. Physicality constraints are checked on the full input-space effects. |
| [verify_converse_operator_coefficients.py](verify_converse_operator_coefficients.py), [converse_operator_checks.json](converse_operator_checks.json) | Reconstructs sphere integrals by Pauli-word monomial integration using exact SymPy matrices. Compares all 18 success/numerator coefficients for three and four inputs; checks the endpoint witness and four-body operator spectra. | Exact coefficient and sign checks. The stabilizer-ray case analysis remains an analytical proof. |
| [check_published_sdp_witness.py](check_published_sdp_witness.py), [published_sdp_witness_results.json](published_sdp_witness_results.json) | Builds normalized symmetric projectors, applies local depolarization and evaluates explicit Choi witnesses in the prior work's Haar objective. | 17 feasible-point checks. This evaluates witnesses for the mathematical formulation; it does not run or reproduce the authors' MATLAB/CVX optimization. |

The construction script defaults to 26 canonical directions and 16 pseudorandom directions, with a fixed seed, at eight polarizations. Its Haar quadrature averages the unnormalized numerator and success separately. The direct joint-map evaluations use the full tensor-product density matrix rather than inserting the closed-form fidelity formula into itself.

## Exact reference values

At retained polarization one third, the construction report checks:

| Quantity | Exact value |
|---|---:|
| Raw fidelity | 2/3 |
| Worst-direction four-copy conditional fidelity | 307/446 |
| Four-copy Haar-average success | 62/405 |
| Four-copy accepted-data Haar fidelity | 43/62 |
| Worst-direction five-copy deterministic gain | 29/8748 |
| Five-copy Haar-average gain | 1/243 |

The three-copy endpoint witness has eigenvalues one fifth, with multiplicity five, and zero, with multiplicity eleven. The four-body input operator, including the identity output factor, has eigenvalues three with multiplicity eight and minus one with multiplicity twenty-four.

The converse checks also include a physical zero-success boundary example: project the first two inputs onto the singlet and return the third. Its average success is $`(1-r^2)/4`$, which vanishes on identical pure inputs. This confirms why the heralded proof uses an unnormalized positive endpoint witness.

## Source comparison and interpretation

The prior universal script is pinned at QuAIR/NonMagic-Purification-codes commit `b50cb1dba98399a1ea8b2ae3cb6bcacd69643ce0`; its released setting has two input copies. The witness script here independently evaluates the four-input mathematical constraints, with explicit nonnegative stabilizer decompositions supplied by the constructions. It does not require a stored list of every stabilizer vertex and yields no optimized fidelity frontier.

All fidelities are pure-target overlaps. Conditional scores are normalized after accepted branches are summed. The lower bound on success and the worst-direction gain follow analytically from the range of the fourth directional moment. See [model and results](../science/model-and-results.md) and [constructions](../science/constructions.md) for the theorem's exact quantifiers.
