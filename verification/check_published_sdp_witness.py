"""Independent evaluation of explicit witnesses in He et al.'s Haar Choi objective.

This is not a reproduction of the authors' MATLAB/CVX optimization.
Q and R are built directly from the normalized symmetric projectors and
local depolarization. No optimization solver or imported author code runs.
"""
from pathlib import Path
import json
import math
from fractions import Fraction
from functools import reduce
import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.diag([1, -1]).astype(complex)
PAULI = [X, Y, Z]

def kron(*xs):
    return reduce(np.kron, xs)

def haar_moment(n):
    answer = np.zeros((2**n, 2**n), complex)
    for weight in range(n+1):
        vec = np.array([int(k.bit_count() == weight) for k in range(2**n)], complex)
        vec /= math.sqrt(math.comb(n, weight))
        answer += np.outer(vec, vec.conj())/(n+1)
    return answer

def local_depolarize(operator, r, n_input, n_total):
    result = operator.copy()
    for qubit in range(n_input):
        nxt = (1+3*r)*result/4
        for p in PAULI:
            unitary = kron(*([I]*qubit + [p] + [I]*(n_total-qubit-1)))
            nxt += (1-r)*(unitary @ result @ unitary.conj().T)/4
        result = nxt
    return result

def moments(n, r):
    Q = local_depolarize(haar_moment(n+1), r, n, n+1)
    R = kron(local_depolarize(haar_moment(n), r, n, n), I)
    return Q, R

def transpose_input(a, n):
    return a.reshape(2**n, 2, 2**n, 2).transpose(2,1,0,3).reshape(a.shape)

def trace_output(a, n):
    return np.einsum("iaja->ij", a.reshape(2**n,2,2**n,2))

def four_filter(axes):
    result = np.zeros((32,32), complex)
    for axis in axes:
        for sign in [-1,1]:
            state = (I+sign*axis)/2
            result += kron(*([state.T]*4), state)/len(axes)
    return result

def passthrough(n):
    result = np.zeros((2**(n+1),2**(n+1)), complex)
    for rest in range(2**(n-1)):
        vec = np.zeros(2**(n+1), complex)
        for bit in [0,1]:
            input_index = bit*2**(n-1)+rest
            vec[2*input_index+bit] = 1
        result += np.outer(vec,vec.conj())
    return result

def at_average_success(J, target, n, r):
    Q,R = moments(n,r)
    current = float(np.trace(transpose_input(J,n) @ R).real)
    if target <= current:
        return J*(target/current)
    weight = (1-target)/(1-current)
    return weight*J+(1-weight)*passthrough(n)

def score(J,n,r):
    Q,R = moments(n,r)
    JT = transpose_input(J,n)
    success = float(np.trace(JT @ R).real)
    numerator = float(np.trace(JT @ Q).real)
    marginal = trace_output(J,n)
    return dict(n=n,r=r,delta=1-r,success=success,numerator=numerator,
                fidelity=numerator/success,raw=(1+r)/2,
                gain=numerator/success-(1+r)/2,
                minimum_J_eigenvalue=float(np.linalg.eigvalsh(J).min()),
                minimum_trace_slack=float(np.linalg.eigvalsh(np.eye(2**n)-marginal).min()),
                trace_J=float(np.trace(J).real))

def five_deterministic():
    result = np.zeros((64,64), complex)
    for axis in PAULI:
        for sign in [-1,1]:
            state = (I+sign*axis)/2
            result += kron(*([state.T]*4), I, state)/3
    failure = np.eye(16)-trace_output(four_filter(PAULI),4)
    phi = np.array([1,0,0,1],complex)
    return result+kron(failure,np.outer(phi,phi.conj()))

reports = []
for r in [0.5,1/3]:
    for name, axes in [("fixed_z", [Z]),("random_pauli",PAULI)]:
        J = four_filter(axes)
        reports.append(dict(name=name,native=True,**score(J,4,r)))
        for target in [0.1,0.5,0.6]:
            reports.append(dict(name=name,target_success=target,**score(at_average_success(J,target,4,r),4,r)))
reports.append(dict(name="five_copy_fallback", **score(five_deterministic(),5,1/3)))
for row in reports:
    assert row["minimum_J_eigenvalue"] > -1e-12
    assert row["minimum_trace_slack"] > -1e-12
    assert row["gain"] > 0
    if "target_success" in row:
        assert abs(row["success"]-row["target_success"]) < 1e-12
for row in reports:
    if row["name"]=="random_pauli" and row.get("native") and row["r"]==1/3:
        assert abs(row["fidelity"]-43/62)<1e-12
        assert abs(row["success"]-62/405)<1e-12
for row in reports:
    if row["name"]=="fixed_z" and row.get("native") and row["r"]==0.5:
        assert abs(row["fidelity"]-547/726)<1e-12
        assert abs(row["success"]-121/640)<1e-12
fallback=reports[-1]
assert abs(fallback["success"]-1)<1e-12
assert abs(fallback["gain"]-1/243)<1e-12
out = Path(__file__).with_name("published_sdp_witness_results.json")
out.write_text(json.dumps({"method":"Independent direct matrix evaluation; no MATLAB/CVX run",
                           "quair_commit":"b50cb1dba98399a1ea8b2ae3cb6bcacd69643ce0",
                           "reports":reports},indent=2)+"\n")
for row in reports:
    print(row["name"],"r=",row["r"],"p=",row["success"],"F=",row["fidelity"],
          "gain=",row["gain"],"minJ=",row["minimum_J_eigenvalue"],
          "minslack=",row["minimum_trace_slack"])

