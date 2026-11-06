#!/usr/bin/env python3
"""Verify the explicit four- and five-input purification constructions.

Only NumPy, SymPy, and the Python standard library are required. For example,
from the repository root:

    python verification/verify_constructions.py \
        --output verification/construction_results.json

The numerical checks evaluate actual joint-input Kraus maps. They are finite
consistency checks, not proofs of the universal gain or the copy converses.
The exact SymPy checks verify the displayed algebra and rational witnesses.
Fidelity throughout means Tr(target * output), not root fidelity.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Any

import numpy as np
import sympy as sp


IDENTITY = np.eye(2, dtype=np.complex128)
PAULIS = np.array(
    [
        [[0, 1], [1, 0]],
        [[0, -1j], [1j, 0]],
        [[1, 0], [0, -1]],
    ],
    dtype=np.complex128,
)
AXES = ("x", "y", "z")
SIGNS = (-1, 1)


def tensor_product(factors: list[np.ndarray]) -> np.ndarray:
    """Kronecker product, preserving the order of the input specimens."""
    result = factors[0]
    for factor in factors[1:]:
        result = np.kron(result, factor)
    return result


def tensor_power(matrix: np.ndarray, copies: int) -> np.ndarray:
    return tensor_product([matrix] * copies)


def eigenstate(axis: str, sign: int) -> np.ndarray:
    """A normalized ket with sigma_axis eigenvalue sign, including Y phases."""
    if axis == "x":
        return np.array([1, sign], dtype=complex) / np.sqrt(2)
    if axis == "y":
        return np.array([1, sign * 1j], dtype=complex) / np.sqrt(2)
    return np.array([1, 0] if sign == 1 else [0, 1], dtype=complex)


def accepted_four_kraus() -> np.ndarray:
    """Six operators K_(a,s) = |a,s><a,s|^tensor4 / sqrt(3), shape 2x16."""
    operators = []
    for axis in AXES:
        for sign in SIGNS:
            ket = eigenstate(axis, sign)
            bra_four = tensor_power(ket, 4).conj()
            operators.append(np.outer(ket, bra_four) / np.sqrt(3))
    return np.stack(operators)


def fallback_five_kraus(accepted: np.ndarray) -> np.ndarray:
    """The full 5-to-1 CPTP map, with 12 success and 42 failure operators.

    Success: K_(a,s) tensor <b|, b=0,1, discards the fifth input.
    Failure: <a,s1;...;a,s4| tensor I / sqrt(3), for each nonunanimous
    pattern, leaves the fifth input as the output. The order is first four,
    then fifth, on every input tensor product.
    """
    operators = []
    for operator in accepted:
        for ket in IDENTITY:
            operators.append(np.kron(operator, ket.conj()[None, :]))
    for axis in AXES:
        for pattern in itertools.product(SIGNS, repeat=4):
            if len(set(pattern)) == 1:
                continue
            bra = tensor_product([eigenstate(axis, s) for s in pattern]).conj()
            operators.append(np.kron(bra[None, :], IDENTITY) / np.sqrt(3))
    return np.stack(operators)


def return_first_four_kraus() -> np.ndarray:
    """Eight Kraus operators for retaining input 1 and tracing inputs 2--4."""
    return np.stack([np.kron(IDENTITY, row[None, :]) for row in np.eye(8)])


def effect(operators: np.ndarray) -> np.ndarray:
    return np.sum(operators.conj().transpose(0, 2, 1) @ operators, axis=0)


def apply_map(operators: np.ndarray, density: np.ndarray) -> np.ndarray:
    return np.sum(
        operators @ density @ operators.conj().transpose(0, 2, 1), axis=0
    )


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def state(direction: np.ndarray, r: float) -> np.ndarray:
    return (IDENTITY + r * np.einsum("a,aij->ij", direction, PAULIS)) / 2


def score(target: np.ndarray, unnormalized: np.ndarray) -> tuple[float, float]:
    success = float(np.trace(unnormalized).real)
    if success <= 0:
        raise ValueError("A tested map has nonpositive success probability.")
    overlap = float(np.trace(target @ unnormalized).real)
    return success, overlap / success


def formulas(direction: np.ndarray, r: float) -> tuple[float, float, float]:
    s4 = float(np.sum(direction**4))
    denominator = 3 + 6 * r**2 + r**4 * s4
    probability = denominator / 24
    conditional = 0.5 + 2 * r * (1 + r**2 * s4) / denominator
    deterministic = (1 + r) / 2 + r * (1 - 6 * r**2 + (4 * r**2 - r**4) * s4) / 48
    return probability, conditional, deterministic


def haar_formulas(r: float) -> tuple[float, float, float]:
    probability = (1 + 2 * r**2 + r**4 / 5) / 8
    conditional = 0.5 + (2 * r / 3 + 2 * r**3 / 5) / (1 + 2 * r**2 + r**4 / 5)
    deterministic = (1 + r) / 2 + r * (1 - 18 * r**2 / 5 - 3 * r**4 / 5) / 48
    return probability, conditional, deterministic


def directions(seed: int, random_count: int) -> list[tuple[str, np.ndarray]]:
    cases = []
    for index, axis in enumerate(AXES):
        for sign in SIGNS:
            vector = np.zeros(3)
            vector[index] = sign
            cases.append((f"axis_{axis}_{sign:+d}", vector))
    for zero in range(3):
        active = [index for index in range(3) if index != zero]
        for signs in itertools.product(SIGNS, repeat=2):
            vector = np.zeros(3)
            vector[active] = np.array(signs) / np.sqrt(2)
            cases.append((f"edge_zero_{AXES[zero]}_{signs}", vector))
    for signs in itertools.product(SIGNS, repeat=3):
        cases.append((f"body_{signs}", np.array(signs) / np.sqrt(3)))
    rng = np.random.default_rng(seed)
    for index, vector in enumerate(rng.normal(size=(random_count, 3))):
        cases.append((f"random_{index:02d}", vector / np.linalg.norm(vector)))
    return cases


def sphere_quadrature() -> list[tuple[float, np.ndarray]]:
    """Normalized spherical integration: four z nodes and twelve azimuths.

    This rule integrates the relevant low-degree polynomial numerators and
    probabilities; conditional fidelities are not averaged before weighting.
    Floating-point evaluation is still reported as a numerical check.
    """
    nodes, weights = np.polynomial.legendre.leggauss(4)
    quadrature = []
    for z, weight in zip(nodes, weights):
        radius = np.sqrt(1 - z * z)
        for index in range(12):
            angle = 2 * np.pi * index / 12
            vector = np.array([radius * np.cos(angle), radius * np.sin(angle), z])
            quadrature.append((float(weight / 24), vector))
    return quadrature


def effect_diagnostics(operators: np.ndarray) -> dict[str, Any]:
    total = effect(operators)
    hermitian = (total + total.conj().T) / 2
    eigenvalues = np.linalg.eigvalsh(hermitian)
    return {
        "kraus_count": len(operators),
        "kraus_shape": list(operators.shape[1:]),
        "hermiticity_error": max_abs(total - total.conj().T),
        "minimum_effect_eigenvalue": float(eigenvalues[0]),
        "maximum_effect_eigenvalue": float(eigenvalues[-1]),
        "minimum_rejection_effect_eigenvalue": float(1 - eigenvalues[-1]),
        "identity_effect_error": max_abs(total - np.eye(total.shape[0])),
    }


def direct_checks(
    accepted: np.ndarray,
    deterministic: np.ndarray,
    cases: list[tuple[str, np.ndarray]],
    r_values: list[float],
) -> dict[str, Any]:
    maxima = dict.fromkeys(
        ["accepted_probability", "accepted_fidelity", "deterministic_fidelity",
         "deterministic_trace", "fallback_density_matrix"], 0.0
    )
    by_r = []
    for r in r_values:
        gains_four, gains_five = [], []
        for _, vector in cases:
            rho, target = state(vector, r), state(vector, 1)
            out_four = apply_map(accepted, tensor_power(rho, 4))
            out_five = apply_map(deterministic, tensor_power(rho, 5))
            probability, fidelity_four = score(target, out_four)
            trace_five, fidelity_five = score(target, out_five)
            predicted_p, predicted_four, predicted_five = formulas(vector, r)
            errors = {
                "accepted_probability": abs(probability - predicted_p),
                "accepted_fidelity": abs(fidelity_four - predicted_four),
                "deterministic_fidelity": abs(fidelity_five - predicted_five),
                "deterministic_trace": abs(trace_five - 1),
                "fallback_density_matrix": max_abs(out_five - out_four - (1 - probability) * rho),
            }
            for name, error in errors.items():
                maxima[name] = max(maxima[name], error)
            gains_four.append(fidelity_four - (1 + r) / 2)
            gains_five.append(fidelity_five - (1 + r) / 2)
        by_r.append({
            "r": r,
            "minimum_gain_over_tested_directions_four": min(gains_four),
            "minimum_gain_over_tested_directions_five": min(gains_five),
        })
    return {"case_count": len(cases) * len(r_values), "maximum_errors": maxima, "by_r": by_r}


def numerical_haar_checks(
    accepted: np.ndarray, deterministic: np.ndarray, r_values: list[float],
    quadrature: list[tuple[float, np.ndarray]],
) -> dict[str, Any]:
    maxima = dict.fromkeys(["accepted_probability", "accepted_haar_fidelity", "deterministic_haar_fidelity"], 0.0)
    rows = []
    for r in r_values:
        p_four = numerator_four = p_five = numerator_five = 0.0
        for weight, vector in quadrature:
            rho, target = state(vector, r), state(vector, 1)
            out_four = apply_map(accepted, tensor_power(rho, 4))
            out_five = apply_map(deterministic, tensor_power(rho, 5))
            p_four += weight * float(np.trace(out_four).real)
            numerator_four += weight * float(np.trace(target @ out_four).real)
            p_five += weight * float(np.trace(out_five).real)
            numerator_five += weight * float(np.trace(target @ out_five).real)
        predicted_p, predicted_four, predicted_five = haar_formulas(r)
        errors = {
            "accepted_probability": abs(p_four - predicted_p),
            "accepted_haar_fidelity": abs(numerator_four / p_four - predicted_four),
            "deterministic_haar_fidelity": abs(numerator_five / p_five - predicted_five),
        }
        for name, error in errors.items():
            maxima[name] = max(maxima[name], error)
        rows.append({"r": r, "average_success": p_four, "average_accepted_overlap_numerator": numerator_four,
                     "accepted_haar_fidelity": numerator_four / p_four,
                     "deterministic_haar_fidelity": numerator_five / p_five})
    return {"quadrature_nodes": len(quadrature), "maximum_errors": maxima, "by_r": rows}


def prescribed_success_checks(
    accepted: np.ndarray, return_first: np.ndarray,
    cases: list[tuple[str, np.ndarray]], r_values: list[float],
    quadrature: list[tuple[float, np.ndarray]],
) -> dict[str, Any]:
    """Check actual thinned/mixed maps, including their average success."""
    maxima = dict.fromkeys(["average_success", "pointwise_success", "conditional_fidelity"], 0.0)
    minimum_effect, maximum_effect = float("inf"), float("-inf")
    rows = []
    for r in r_values:
        p0, _, _ = haar_formulas(r)
        haar_input = np.zeros((16, 16), dtype=complex)
        for weight, vector in quadrature:
            haar_input += weight * tensor_power(state(vector, r), 4)
        for requested in [p0 / 2, p0, (1 + p0) / 2, 0.95, 1.0]:
            if requested <= p0:
                method, weight = "independent thinning", requested / p0
                operators = np.sqrt(weight) * accepted
            else:
                method, weight = "mix with return-first channel", (1 - requested) / (1 - p0)
                operators = np.concatenate([np.sqrt(weight) * accepted,
                                            np.sqrt(1 - weight) * return_first])
            diagnostic = effect_diagnostics(operators)
            minimum_effect = min(minimum_effect, diagnostic["minimum_effect_eigenvalue"])
            maximum_effect = max(maximum_effect, diagnostic["maximum_effect_eigenvalue"])
            average_success = float(np.trace(apply_map(operators, haar_input)).real)
            maxima["average_success"] = max(maxima["average_success"], abs(average_success - requested))
            gains = []
            for _, vector in cases:
                rho, target = state(vector, r), state(vector, 1)
                actual_p, actual_f = score(target, apply_map(operators, tensor_power(rho, 4)))
                bare_p, bare_f, _ = formulas(vector, r)
                raw_f = (1 + r) / 2
                if requested <= p0:
                    predicted_p, predicted_f = weight * bare_p, bare_f
                else:
                    predicted_p = weight * bare_p + 1 - weight
                    predicted_f = raw_f + weight * bare_p * (bare_f - raw_f) / predicted_p
                maxima["pointwise_success"] = max(maxima["pointwise_success"], abs(actual_p - predicted_p))
                maxima["conditional_fidelity"] = max(maxima["conditional_fidelity"], abs(actual_f - predicted_f))
                gains.append(actual_f - raw_f)
            rows.append({"r": r, "requested_average_success": requested, "method": method,
                         "thinning_probability_or_filter_mixture_weight": weight,
                         "actual_average_success": average_success,
                         "minimum_gain_over_tested_directions": min(gains)})
    return {"case_count": len(rows) * len(cases), "maximum_errors": maxima,
            "minimum_effect_eigenvalue": minimum_effect, "maximum_effect_eigenvalue": maximum_effect,
            "variants": rows}


def exact_sphere_average(expression: sp.Expr, coordinates: tuple[sp.Symbol, ...]) -> sp.Expr:
    """Uniform S^2 monomial moments; odd powers vanish."""
    average = sp.S.Zero
    for exponents, coefficient in sp.Poly(sp.expand(expression), *coordinates).terms():
        if any(power % 2 for power in exponents):
            continue
        moment = sp.prod(sp.factorial2(power - 1) for power in exponents)
        moment /= sp.factorial2(sum(exponents) + 1)
        average += coefficient * moment
    return sp.factor(average)


def symbolic_checks() -> dict[str, Any]:
    r, s4, requested = sp.symbols("r s4 p", real=True)
    coordinates = sp.symbols("u_x u_y u_z", real=True)
    denominator = 3 + 6 * r**2 + r**4 * s4
    probability = denominator / 24
    raw = (1 + r) / 2
    conditional = sp.Rational(1, 2) + 2 * r * (1 + r**2 * s4) / denominator
    numerator = sp.cancel(probability * conditional)
    gain_four = r * (1 - 6 * r**2 + (4 * r**2 - r**4) * s4) / (2 * denominator)
    gain_five = r * (1 - 6 * r**2 + (4 * r**2 - r**4) * s4) / 48
    deterministic = probability * conditional + (1 - probability) * raw

    # Integrate unnormalized branch probabilities and overlaps separately.
    branch_probabilities = [((1 + sign * r * u) / 2)**4 / 3
                            for u in coordinates for sign in SIGNS]
    branch_overlaps = [p * (1 + sign * u) / 2
                       for p, (u, sign) in zip(branch_probabilities,
                                               itertools.product(coordinates, SIGNS))]
    p0 = exact_sphere_average(sum(branch_probabilities), coordinates)
    haar_numerator = exact_sphere_average(sum(branch_overlaps), coordinates)
    haar_fidelity = sp.cancel(haar_numerator / p0)
    haar_deterministic = sp.cancel(haar_numerator + (1 - p0) * raw)
    p0_claim = (1 + 2 * r**2 + r**4 / 5) / 8
    haar_claim = sp.Rational(1, 2) + (2 * r / 3 + 2 * r**3 / 5) / (1 + 2 * r**2 + r**4 / 5)

    thinning = requested / p0
    lam = (1 - requested) / (1 - p0)
    mixed_p = lam * probability + 1 - lam
    mixed_numerator = lam * numerator + (1 - lam) * raw
    mixed_gain = lam * probability * gain_four / mixed_p
    boundary = sp.sqrt(-7 + 2 * sp.sqrt(13))
    identities = {
        "conditional_gain": sp.cancel(conditional - raw - gain_four) == 0,
        "fallback_gain": sp.cancel(deterministic - raw - gain_five) == 0,
        "haar_success_from_branch_moments": sp.cancel(p0 - p0_claim) == 0,
        "haar_fidelity_from_weighted_branch_moments": sp.cancel(haar_fidelity - haar_claim) == 0,
        "haar_deterministic_fidelity": sp.cancel(haar_deterministic - (raw + gain_five.subs(s4, sp.Rational(3, 5)))) == 0,
        "thinning_preserves_conditional_fidelity": sp.cancel(thinning * numerator / (thinning * probability) - conditional) == 0,
        "thinning_has_requested_average_success": sp.cancel(thinning * p0 - requested) == 0,
        "mixture_has_requested_average_success": sp.cancel(lam * p0 + 1 - lam - requested) == 0,
        "mixture_pointwise_gain_formula": sp.cancel(mixed_numerator / mixed_p - raw - mixed_gain) == 0,
        "mixture_probability_one_has_zero_gain": sp.cancel(mixed_gain.subs(requested, 1)) == 0,
        "pointwise_boundary_polynomial": sp.simplify(3 - 14 * boundary**2 - boundary**4) == 0,
    }
    at_third = {r: sp.Rational(1, 3)}
    worst = {s4: sp.Rational(1, 3), **at_third}
    computed = {
        "raw_fidelity": raw.subs(at_third),
        "minimum_success": probability.subs(worst),
        "maximum_success": probability.subs({s4: 1, **at_third}),
        "worst_conditional_fidelity": conditional.subs(worst),
        "worst_conditional_gain": gain_four.subs(worst),
        "haar_success": p0.subs(at_third),
        "haar_conditional_fidelity": haar_fidelity.subs(at_third),
        "haar_conditional_gain": (haar_fidelity - raw).subs(at_third),
        "worst_deterministic_gain": gain_five.subs(worst),
        "haar_deterministic_gain": (haar_deterministic - raw).subs(at_third),
    }
    expected = dict(zip(computed, ["2/3", "223/1458", "149/972", "307/446", "29/1338",
                                   "62/405", "43/62", "5/186", "29/8748", "1/243"]))
    witnesses = {name: {"computed": str(sp.factor(value)), "expected": expected[name],
                        "matches": sp.simplify(value - sp.Rational(expected[name])) == 0}
                 for name, value in computed.items()}
    expressions = {
        "pointwise_success": probability, "conditional_fidelity": conditional,
        "conditional_gain": gain_four, "deterministic_gain": gain_five,
        "haar_success": p0, "haar_accepted_overlap_numerator": haar_numerator,
        "haar_conditional_fidelity": haar_fidelity,
        "haar_deterministic_fidelity": haar_deterministic,
        "thinning_probability_for_p_le_p0": thinning,
        "filter_mixture_weight_for_p_gt_p0": lam,
        "mixture_pointwise_success": mixed_p, "mixture_pointwise_gain": mixed_gain,
        "mixture_haar_fidelity": (lam * haar_numerator + (1 - lam) * raw) / requested,
    }
    return {"identities": identities, "rational_witness_at_r_one_third": witnesses,
            "expressions": {name: str(sp.factor(value)) for name, value in expressions.items()},
            "pointwise_boundary": str(boundary), "pointwise_boundary_decimal": float(boundary),
            "scope": "Exact algebra and moments; these checks do not prove the stabilizer-cone converse inequalities."}


def run(seed: int, random_count: int, tolerance: float) -> dict[str, Any]:
    accepted = accepted_four_kraus()
    deterministic = fallback_five_kraus(accepted)
    return_first = return_first_four_kraus()
    cases, quadrature = directions(seed, random_count), sphere_quadrature()
    boundary = float(sp.sqrt(-7 + 2 * sp.sqrt(13)))
    r_values = [0.0, 0.1, 1 / 3, boundary - 1e-4, boundary, boundary + 1e-4, 0.7, 1.0]
    effects = {"accepted_four": effect_diagnostics(accepted),
               "deterministic_five": effect_diagnostics(deterministic),
               "return_first_four": effect_diagnostics(return_first)}
    direct = direct_checks(accepted, deterministic, cases, r_values)
    haar = numerical_haar_checks(accepted, deterministic, r_values, quadrature)
    prescribed = prescribed_success_checks(accepted, return_first, cases,
                                            [0.1, 1 / 3, boundary - 1e-4], quadrature)
    exact = symbolic_checks()

    checks = {
        "six_accepted_operators_of_shape_2_by_16": accepted.shape == (6, 2, 16),
        "fifty_four_fallback_operators_of_shape_2_by_32": deterministic.shape == (54, 2, 32),
        "accepted_effect_is_psd": effects["accepted_four"]["minimum_effect_eigenvalue"] >= -tolerance,
        "accepted_effect_is_at_most_identity": effects["accepted_four"]["minimum_rejection_effect_eigenvalue"] >= -tolerance,
        "five_input_effect_is_identity": effects["deterministic_five"]["identity_effect_error"] <= tolerance,
        "return_first_effect_is_identity": effects["return_first_four"]["identity_effect_error"] <= tolerance,
        "effects_are_hermitian": all(item["hermiticity_error"] <= tolerance for item in effects.values()),
        "direct_joint_map_formulas_agree": max(direct["maximum_errors"].values()) <= tolerance,
        "haar_formulas_agree": max(haar["maximum_errors"].values()) <= tolerance,
        "prescribed_success_formulas_agree": max(prescribed["maximum_errors"].values()) <= tolerance,
        "prescribed_success_effects_are_psd": prescribed["minimum_effect_eigenvalue"] >= -tolerance,
        "prescribed_success_effects_are_at_most_identity": prescribed["maximum_effect_eigenvalue"] <= 1 + tolerance,
        "exact_symbolic_identities": all(exact["identities"].values()),
        "exact_rational_witnesses": all(item["matches"] for item in exact["rational_witness_at_r_one_third"].values()),
    }
    return {
        "schema_version": 1,
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "configuration": {"seed": seed, "random_directions": random_count, "canonical_directions": 26,
                          "total_directions": len(cases), "r_values": r_values, "tolerance": tolerance,
                          "numpy_version": np.__version__, "sympy_version": sp.__version__},
        "physicality": effects,
        "direct_joint_input_checks": direct,
        "haar_checks": haar,
        "prescribed_average_success_checks": prescribed,
        "exact_symbolic_checks": exact,
        "interpretation": [
            "All numerical maps are evaluated from actual 4-input or 5-input Kraus operators.",
            "The five-input Kraus list covers every measurement record, including failure and the discarded fifth input on success.",
            "Success-weighted Haar numerators are averaged before dividing; root fidelity is never substituted.",
            "Finite directions and floating-point physicality checks are consistency evidence, not universal proofs.",
            "The analytic theorem uses the S4 range and stabilizer-cone converse arguments in the science files.",
            "The r=0 and r=1 endpoints and values above r_star are diagnostics, not claimed strict-gain points.",
            "The prescribed-success check includes p=1, where the four-input mixture returns a raw input and has zero gain.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output", type=Path, help="Write the complete results JSON to this path; otherwise print it.")
    parser.add_argument("--seed", type=int, default=34316, help="Seed for the modest random direction sample.")
    parser.add_argument("--random-directions", type=int, default=16, help="Random directions in addition to 26 canonical directions.")
    parser.add_argument("--tolerance", type=float, default=1e-11, help="Absolute tolerance for finite numerical checks.")
    args = parser.parse_args()
    if args.random_directions < 0 or not np.isfinite(args.tolerance) or args.tolerance <= 0:
        parser.error("random-directions must be nonnegative and tolerance must be finite and positive")
    result = run(args.seed, args.random_directions, args.tolerance)
    rendered = json.dumps(result, indent=2, allow_nan=False) + "\n"
    if args.output is None:
        print(rendered, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(json.dumps({"status": result["status"], "output": str(args.output),
                          "direct_cases": result["direct_joint_input_checks"]["case_count"],
                          "prescribed_success_cases": result["prescribed_average_success_checks"]["case_count"],
                          "maximum_direct_errors": result["direct_joint_input_checks"]["maximum_errors"],
                          "failed_checks": [name for name, passed in result["checks"].items() if not passed]}, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
