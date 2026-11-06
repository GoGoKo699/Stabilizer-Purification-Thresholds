"""Exact finite-dimensional checks of the converse moment identities.

The sphere integrals are reconstructed by enumerating Pauli words and applying
the general monomial moment formula. They are then compared with the compact
operators in the two proof pages. This checks coefficients and transpose signs;
the stabilizer inequalities are proved analytically in those pages.
"""

from collections import Counter
from functools import lru_cache
from itertools import combinations, product
import json
from pathlib import Path

import sympy as sp


PAULI = (
    sp.eye(2),
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.diag(1, -1),
)
TRANSPOSE_SIGN = (1, 1, -1, 1)


@lru_cache(maxsize=None)
def pauli_word(word):
    result = sp.ones(1, 1)
    for index in word:
        result = sp.kronecker_product(result, PAULI[index])
    return sp.ImmutableMatrix(result)


def sphere_moment(indices):
    counts = Counter(indices)
    if any(count % 2 for count in counts.values()):
        return sp.S.Zero
    numerator = sp.prod(sp.factorial2(count - 1) for count in counts.values())
    return numerator / sp.factorial2(sum(counts.values()) + 1)


def integrated_coefficients(n, with_target):
    """Return coefficients by input degree of the actual normalized integral."""
    dimension = 2 ** (n + 1)
    coefficients = [sp.zeros(dimension) for _ in range(n + 1)]
    output_indices = range(4) if with_target else (0,)
    normalization = sp.Rational(1, 2 ** (n + int(with_target)))
    for inputs in product(range(4), repeat=n):
        degree = sum(index != 0 for index in inputs)
        transpose_sign = sp.prod(TRANSPOSE_SIGN[index] for index in inputs)
        for output in output_indices:
            indices = [index for index in inputs if index]
            if output:
                indices.append(output)
            scalar = normalization * transpose_sign * sphere_moment(indices)
            if scalar:
                coefficients[degree] += scalar * pauli_word(inputs + (output,))
    return coefficients


def supported_pauli(n, factors):
    word = [0] * (n + 1)
    for qubit, axis in factors.items():
        word[qubit] = axis
    return pauli_word(tuple(word))


def compact_operators(n):
    dimension = 2 ** (n + 1)
    a_op, b_op, c_op = (sp.zeros(dimension) for _ in range(3))
    for i, k in combinations(range(n), 2):
        for axis in (1, 2, 3):
            a_op += supported_pauli(n, {i: axis, k: axis})
    for i in range(n):
        for axis in (1, 2, 3):
            b_op += TRANSPOSE_SIGN[axis] * supported_pauli(n, {i: axis, n: axis})
    for triple in combinations(range(n), 3):
        for k in triple:
            i, ell = (index for index in triple if index != k)
            for axis_a, axis_b in product((1, 2, 3), repeat=2):
                c_op += TRANSPOSE_SIGN[axis_b] * supported_pauli(
                    n, {i: axis_a, ell: axis_a, k: axis_b, n: axis_b}
                )
    return a_op, b_op, c_op


def zero_matrix(matrix):
    return matrix == sp.zeros(matrix.rows, matrix.cols)


checks = {}
for n in (3, 4):
    dimension = 2 ** (n + 1)
    identity = sp.eye(dimension)
    a_op, b_op, c_op = compact_operators(n)
    denominator = integrated_coefficients(n, with_target=False)
    numerator = integrated_coefficients(n, with_target=True)
    expected_denominator = [sp.zeros(dimension) for _ in range(n + 1)]
    expected_numerator = [sp.zeros(dimension) for _ in range(n + 1)]
    expected_denominator[0] = identity / 2**n
    expected_denominator[2] = a_op / (3 * 2**n)
    expected_numerator[0] = identity / 2 ** (n + 1)
    expected_numerator[1] = b_op / (3 * 2 ** (n + 1))
    expected_numerator[2] = a_op / (3 * 2 ** (n + 1))
    expected_numerator[3] = c_op / (15 * 2 ** (n + 1))
    if n == 4:
        t_op = sp.zeros(dimension)
        pairings = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
        for first, second in pairings:
            for axis_a, axis_b in product((1, 2, 3), repeat=2):
                t_op += supported_pauli(
                    n,
                    {
                        first[0]: axis_a,
                        first[1]: axis_a,
                        second[0]: axis_b,
                        second[1]: axis_b,
                    },
                )
        expected_denominator[4] = t_op / (15 * 2**n)
        expected_numerator[4] = t_op / (15 * 2 ** (n + 1))
    for degree in range(n + 1):
        checks[f"n{n}_success_degree{degree}"] = zero_matrix(
            denominator[degree] - expected_denominator[degree]
        )
        checks[f"n{n}_numerator_degree{degree}"] = zero_matrix(
            numerator[degree] - expected_numerator[degree]
        )
    if n == 3:
        witness = sum(denominator, sp.zeros(dimension)) - sum(
            numerator, sp.zeros(dimension)
        )
        expected_witness = (identity + a_op / 3 - b_op / 3 - c_op / 15) / 16
        checks["n3_pure_endpoint_witness_identity"] = zero_matrix(
            witness - expected_witness
        )
        eigenvalues = witness.eigenvals()
        checks["n3_pure_endpoint_witness_positive"] = all(
            value >= 0 for value in eigenvalues
        )
        checks["n3_pure_endpoint_witness_eigenvalues"] = {
            str(value): multiplicity for value, multiplicity in eigenvalues.items()
        }
        # A physically allowed branch with zero success on every pure identical
        # input: Bell-project inputs 1,2 onto the singlet and return input 3.
        singlet = sp.Matrix([0, 1, -1, 0])
        bell = sp.Matrix([1, 0, 0, 1])
        boundary_state = sp.kronecker_product(
            singlet * singlet.T / 2, bell * bell.T / 2
        )
        boundary_coefficients = {
            "A": sp.trace(boundary_state * a_op),
            "B": sp.trace(boundary_state * b_op),
            "C": sp.trace(boundary_state * c_op),
        }
        checks["n3_zero_success_boundary_example"] = {
            key: str(value) for key, value in boundary_coefficients.items()
        }
        checks["n3_zero_success_boundary_example_coefficients"] = (
            boundary_coefficients == {"A": -3, "B": 3, "C": -15}
        )
    else:
        k_ops = [supported_pauli(n, {i: axis for i in range(n)}) for axis in (1, 2, 3)]
        checks["four_input_pauli_product"] = zero_matrix(k_ops[0] * k_ops[1] - k_ops[2])
        d_op = sum(k_ops, sp.zeros(dimension))
        checks["four_input_D_spectrum"] = {
            str(value): multiplicity for value, multiplicity in d_op.eigenvals().items()
        }

assert all(value for value in checks.values() if isinstance(value, bool))
output = {
    "method": "Exact SymPy matrix equalities; Pauli-word sphere integration reconstructed independently of the compact formulas.",
    "checks": checks,
    "limits": "Checks coefficient identities and selected endpoint/operator spectra. It does not replace the analytic stabilizer-ray case proofs or constitute a literature priority check.",
}
output_path = Path(__file__).with_name("converse_operator_checks.json")
output_path.write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps(output, indent=2))
