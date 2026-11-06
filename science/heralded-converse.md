# Heralded converse with three inputs

## Setting and theorem

Let

```math
\rho_{\mathbf u}(r)=\frac{I+r\,\mathbf u\cdot\boldsymbol\sigma}{2},
\qquad
\psi_{\mathbf u}=\frac{I+\mathbf u\cdot\boldsymbol\sigma}{2},
\qquad
\mathbf u\in S^2,\quad 0\lt r\lt 1.
\tag{H1}
```

The input consists of identical, independent copies of $`\rho_{\mathbf u}(r)`$. The direction $`\mathbf u`$ is unknown; the target is its principal eigenstate $`\psi_{\mathbf u}`$. The fidelity of an unprocessed copy is

```math
F_0(r)=\mathrm{tr}\bigl[\psi_{\mathbf u}\rho_{\mathbf u}(r)\bigr]
=\frac{1+r}{2}.
\tag{H2}
```

A heralded protocol is represented by its accepted completely positive, trace-nonincreasing map $`\mathcal E`$ from $`n`$ input qubits to one output qubit. All accepted measurement outcomes and classical choices are included in this map. It may depend on $`r`$, but not on the unknown direction. We write

```math
\begin{aligned}
p_{\mathcal E}(\mathbf u,r)
&=\mathrm{tr}\mathcal E\bigl(\rho_{\mathbf u}(r)^{\otimes n}\bigr),\\
N_{\mathcal E}(r)
&=\int_{S^2}\mathrm{tr}\!\left[
\psi_{\mathbf u}\mathcal E\bigl(\rho_{\mathbf u}(r)^{\otimes n}\bigr)
\right]d\mu(\mathbf u),\\
p_{\mathcal E}(r)
&=\int_{S^2}p_{\mathcal E}(\mathbf u,r)\,d\mu(\mathbf u),\\
F_{\mathcal E}(r)&=\frac{N_{\mathcal E}(r)}{p_{\mathcal E}(r)}.
\end{aligned}
\tag{H3}
```

Here $`\mu`$ is normalized uniform measure on the sphere. Thus $`F_{\mathcal E}`$ is fidelity averaged over accepted data: it is a ratio of Haar averages, rather than the Haar average of the separately normalized conditional fidelities. No direction-independent success or rotational covariance is assumed.

Let $`\mathrm{STAB}_m`$ be the convex hull of pure $`m`$-qubit stabilizer projectors, and let

```math
\mathsf K_m=\{\lambda\omega:\lambda\ge0,\ \omega\in\mathrm{STAB}_m\}
\tag{H4}
```

be its positive cone. The allowed class consists of accepted maps whose Choi operators belong to $`\mathsf K_{n+1}`$. This is the subnormalized completely stabilizer-preserving class, defined precisely below; it includes ordinary stabilizer instruments.

**Theorem H.** For every $`n\in\{1,2,3\}`$, every $`0\lt r\lt 1`$, and every nonzero accepted map in this class,

```math
F_{\mathcal E}(r)\le\frac{1+r}{2}.
\tag{H5}
```

For each prescribed average success probability $`p\in(0,1]`$, equality is attained by an ordinary stabilizer protocol. Consequently, the optimal conditional Haar fidelity at that success probability is exactly $`(1+r)/2`$.

The two-copy qubit case was established by He et al. [1, Theorem 2]. The argument below proves the three-copy bound and therefore also covers fewer copies. Its statewise consequence is that no such protocol with at most three copies can strictly improve fidelity for every unknown direction.

## Choi convention and the free class

Write $`A=A_1\cdots A_n`$ for the input reference and $`o`$ for the output. In the computational basis, use the unnormalized maximally entangled vector

```math
|\Omega_n\rangle=\sum_{x\in\{0,1\}^n}|x\rangle_A|x\rangle_{A'},
\qquad
J_{\mathcal E}=(\mathrm{id}_A\otimes\mathcal E)
\bigl(|\Omega_n\rangle\langle\Omega_n|\bigr).
\tag{H6}
```

The conventions are therefore

```math
\begin{aligned}
\mathcal E(X)&=\mathrm{tr}_A\!\left[(X^T\otimes I_o)J_{\mathcal E}\right],\\
\mathrm{tr}\bigl[Y\mathcal E(X)\bigr]
&=\mathrm{tr}\bigl[J_{\mathcal E}(X^T\otimes Y)\bigr],\\
J_{\mathcal E}&\ge0,\qquad
\mathrm{tr}_oJ_{\mathcal E}\le I_A.
\end{aligned}
\tag{H7}
```

The last two conditions are complete positivity and trace nonincrease. Equality in the last condition characterizes a channel. For a nonzero accepted map, set

```math
\tau=\mathrm{tr}J_{\mathcal E}\gt 0,
\qquad j=J_{\mathcal E}/\tau.
\tag{H8}
```

The state $`j`$ is normalized. In a heralded protocol, $`\tau`$ need not equal $`2^n`$, and $`J_{\mathcal E}/2^n`$ need not be normalized.

The condition $`J_{\mathcal E}\in\mathsf K_{n+1}`$ is equivalent to preservation of the stabilizer cone even when the map acts on part of a larger system. Necessity follows by applying the map to halves of $`n`$ Bell pairs, a stabilizer input: the resulting operator is $`J_{\mathcal E}/2^n`$. For sufficiency, let $`\omega_{RA'}`$ be a stabilizer operator and let $`|\Phi_n\rangle=2^{-n/2}|\Omega_n\rangle`$. The Bell-projection link product satisfies

```math
{}_{A'A}\langle\Phi_n|
\bigl(\omega_{RA'}\otimes J_{\mathcal E,Ao}\bigr)
|\Phi_n\rangle_{A'A}
=2^{-n}(\mathrm{id}_R\otimes\mathcal E)(\omega_{RA'}).
```

Tensor products, Bell projection, partial trace, and positive mixtures preserve the stabilizer cone. The positive rescaling by $`2^n`$ does not affect cone membership, proving sufficiency. This is a characterization of the full cone-preserving comparison class; the matching constructions use ordinary stabilizer instruments within that class.

In particular, Clifford gates, stabilizer ancillas, Pauli measurements, classical randomness and feedforward, discarding, and acceptance of any collection of measurement outcomes yield Choi operators in this cone. One can also see the required inclusion directly by applying such a complete accepted instrument to halves of Bell pairs. The converse therefore allows arbitrary ordinary stabilizer circuits, not only the measurement construction used for achievability.

There is no zero-success issue inside $`0\lt r\lt 1`$. Since

```math
\bigl(\rho_{\mathbf u}(r)^T\bigr)^{\otimes n}
\ge \left(\frac{1-r}{2}\right)^n I_A,
```

positivity of $`J_{\mathcal E}`$ gives the uniform bound

```math
p_{\mathcal E}(\mathbf u,r)
\ge\tau\left(\frac{1-r}{2}\right)^n\gt 0.
\tag{H9}
```

This permits normalization at every direction for every nonzero accepted map.

## Exact three-copy Haar expansion

We now take $`n=3`$. Write $`\langle O\rangle=\mathrm{tr}(jO)`$. Identity factors on qubits outside an operator's stated support are implicit. The transpose signs are

```math
\sigma_a^T=t_a\sigma_a,
\qquad t_x=t_z=1,\quad t_y=-1.
\tag{H10}
```

Define the operators

```math
\begin{aligned}
\mathsf A_3
&=\sum_{1\le i\lt k\le3}\sum_{a=x,y,z}
\sigma_a^{(i)}\sigma_a^{(k)},\\
\mathsf B_3
&=\sum_{i=1}^3\sum_{a=x,y,z}
t_a\sigma_a^{(i)}\sigma_a^{(o)},\\
\mathsf C_3
&=\sum_{k=1}^3\sum_{a,b=x,y,z}
t_b\sigma_a^{(i)}\sigma_a^{(\ell)}
\sigma_b^{(k)}\sigma_b^{(o)},
\qquad \{i,\ell\}=\{1,2,3\}\setminus\{k\}.
\end{aligned}
\tag{H11}
```

The order of $`i,\ell`$ in the last line is immaterial. Put $`A=\langle\mathsf A_3\rangle`$, $`B=\langle\mathsf B_3\rangle`$, and $`C=\langle\mathsf C_3\rangle`$.

The required sphere moments are

```math
\int u_a\,d\mu=0,\qquad
\int u_a u_b\,d\mu=\frac{\delta_{ab}}3,
\qquad
\int u_a u_b u_c u_d\,d\mu
=\frac{\delta_{ab}\delta_{cd}+\delta_{ac}\delta_{bd}
+\delta_{ad}\delta_{bc}}{15}.
\tag{H12}
```

Odd moments vanish. Expanding each input factor in Pauli operators and using (H7) and (H12) gives

```math
\begin{aligned}
p_{\mathcal E}(r)
&=\frac{\tau}{8}\left(1+\frac A3r^2\right),\\
N_{\mathcal E}(r)
&=\frac{\tau}{16}\left(
1+\frac A3r^2+\frac B3r+\frac C{15}r^3
\right).
\end{aligned}
\tag{H13}
```

In $`\mathsf A_3`$, both transposed inputs carry the same Pauli index, so their two transpose signs cancel. In $`\mathsf C_3`$, the input paired with the output carries the single remaining sign $`t_b`$. All three pairings of the fourth sphere moment are included in (H11), including their multiplicities when $`a=b`$.

Set $`d_3(r)=1+Ar^2/3`$. Equations (H3) and (H13) imply

```math
F_{\mathcal E}(r)-\frac{1+r}{2}
=\frac{r}{2d_3(r)}q(r^2),
\qquad
q(s)=\left(\frac B3-1\right)
+\left(\frac C{15}-\frac A3\right)s.
\tag{H14}
```

By (H9), $`d_3(r)\ge(1-r)^3\gt 0`$ for $`r\lt 1`$. The sign of the fidelity gain is therefore the sign of an affine function of $`r^2`$.

## The stabilizer correlation bound

**Lemma H1.** Every four-qubit stabilizer mixture satisfies

```math
\langle\mathsf B_3\rangle\le3.
\tag{H15}
```

**Proof.** It suffices to consider a pure stabilizer state. Every Hermitian Pauli expectation in such a state belongs to $`\{0,+1,-1\}`$; a nonzero expectation means that the state is an eigenvector of that Pauli.

Suppose first that some input $`i`$ has two nonzero correlations among
$`X_iX_o`$, $`Y_iY_o`$, and $`Z_iZ_o`$. Any two of these commuting, independent pair Paulis have a one-dimensional common eigenspace on qubits $`i,o`$: one of the Bell states. The full pure state therefore factors into that Bell state and a state of the remaining inputs. The output's single-qubit Pauli expectations vanish, so all correlations between it and other inputs vanish. The isolated pair contributes at most three to $`\mathsf B_3`$.

Otherwise, each of the three inputs has at most one nonzero correlation in the displayed list. Its signed contribution to $`\mathsf B_3`$ is at most one, and their sum is at most three. Convexity proves the claim for stabilizer mixtures. $`\square`$

It follows that $`q(0)=B/3-1\le0`$.

## The pure-state endpoint, including zero success

At $`r=1`$, a particular accepted map may have zero success on some or all pure inputs. The argument must therefore use unnormalized quantities rather than a conditional fidelity at that endpoint.

Consider the positive semidefinite operator

```math
W_3=\int_{S^2}
(\psi_{\mathbf u}^T)^{\otimes3}\otimes(I-\psi_{\mathbf u})
\,d\mu(\mathbf u)\ge0.
\tag{H16}
```

The same moment expansion gives the exact identity

```math
W_3=\frac1{16}
\left(I+\frac{\mathsf A_3}{3}
-\frac{\mathsf B_3}{3}-\frac{\mathsf C_3}{15}\right).
\tag{H17}
```

Consequently,

```math
0\le16\mathrm{tr}(jW_3)
=1+\frac A3-\frac B3-\frac C{15}
=-q(1).
\tag{H18}
```

This remains valid if both the success and fidelity numerators vanish at $`r=1`$. Together with Lemma H1 it yields

```math
q(s)=(1-s)q(0)+s q(1)\le0,
\qquad 0\le s\le1.
\tag{H19}
```

Substitution into (H14) proves the three-copy bound. The map $`\mathcal E`$ is held fixed during this interpolation. Since the bound holds for every such map, it also holds when a protocol is chosen using the actual noise parameter $`r`$.

## Fewer copies and equality at every success probability

An allowed protocol on one or two inputs can be regarded as a three-input protocol that discards unused inputs. This preserves complete positivity, trace nonincrease, and membership of the Choi stabilizer cone: the additional reference factors in its Choi operator are identities, which are positive mixtures of stabilizer projectors. Thus the three-copy bound implies (H5) for all $`n\le3`$.

For any $`n\ge1`$ and any $`p\in(0,1]`$, the map

```math
\mathcal E_p(X)=p\,\mathrm{tr}_{A_2\cdots A_n}X
\tag{H20}
```

returns the first input and accepts with an independent classical probability $`p`$. Its Choi operator is

```math
J_{\mathcal E_p}
=p\,|\Omega_1\rangle\langle\Omega_1|_{A_1o}
\otimes I_{A_2\cdots A_n},
\tag{H21}
```

up to the stated tensor-factor ordering. This lies in the stabilizer cone and has $`\mathrm{tr}_oJ_{\mathcal E_p}=pI_A`$. Its success is $`p`$ at every direction and its conditional output is exactly $`\rho_{\mathbf u}(r)`$. It attains (H5) at every prescribed average success probability, completing Theorem H.

## Statewise consequence and the four-copy onset

For $`r\lt 1`$, let

```math
f_{\mathcal E}(\mathbf u,r)
=\frac{\mathrm{tr}\!\left[
\psi_{\mathbf u}\mathcal E(\rho_{\mathbf u}(r)^{\otimes n})
\right]}{p_{\mathcal E}(\mathbf u,r)}.
```

The positive-success bound (H9) makes this well defined. The Haar gap satisfies

```math
p_{\mathcal E}(r)\bigl[F_{\mathcal E}(r)-F_0(r)\bigr]
=\int p_{\mathcal E}(\mathbf u,r)
\bigl[f_{\mathcal E}(\mathbf u,r)-F_0(r)\bigr]\,d\mu(\mathbf u).
\tag{H22}
```

Strict improvement for every direction would make the right-hand side positive. Theorem H therefore rules out that stronger form of universal purification with at most three copies.

The [four-copy construction](constructions.md) is an ordinary stabilizer instrument that strictly improves every direction for

```math
0\lt r\lt r_*:=\sqrt{-7+2\sqrt{13}}.
```

Together with Theorem H, it makes the minimum heralded input-copy budget exactly four throughout this interval. Thus four is the first copy count permitting universal gain for at least one polarization in $`0\lt r\lt 1`$. The construction's copy cost, success probability, and attribution are given on its own page. This result does not classify the minimum budget outside the displayed interval or optimize fidelity at fixed success. The corresponding deterministic minimum is five, as established by the [deterministic converse](deterministic-converse.md) and the five-copy construction.

## References


1. K. He, C. Zhu, H. Yao, J. Liu, Y. Li, and X. Wang, *No-Go Theorems for Universal Quantum State Purification via Classically Simulable Operations*, Physical Review Letters **136**, 090204 (2026), [DOI: 10.1103/bdw8-k91v](https://doi.org/10.1103/bdw8-k91v). [Available full preprint, arXiv:2504.10516v2](https://arxiv.org/html/2504.10516v2), especially Eqs. (2), (3), Theorem 2, and Appendix Eq. (S25).
