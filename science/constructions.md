# Four-copy filtering and a fifth-copy fallback

The local unanimity filter is an instance of the abstention method described by [Gendra et al. (2012), Sec. 3.2](https://arxiv.org/html/1205.5479v1). Randomizing it over the three Pauli axes gives a simple guarantee for every target direction. Keeping a spare noisy input then converts that conditional gain into an unconditional one.

The input, fidelity and Choi conventions are fixed in [model and results](model-and-results.md).

## The accepted four-copy operation

Choose $a\in\{x,y,z\}$ uniformly and measure all four inputs in that Pauli basis. Accept exactly when all four signs agree. If the common sign is $s\in\{-1,1\}$, retain a measured copy in the state

$$
P_{a,s}=\frac{I+s\sigma_a}{2}.
$$

The resulting accepted map is

$$
\mathcal E_4(A)=\frac13\sum_{a,s}\operatorname{tr}(P_{a,s}^{\otimes4}A)P_{a,s}.
$$

Its Kraus operators are $K_{a,s}=3^{-1/2}|a,s\rangle\langle a,s|^{\otimes4}$. For each axis, the two accepted outcome projectors are orthogonal, so their sum is at most the identity. Averaging the three axes gives $\sum K_{a,s}^\dagger K_{a,s}\le I$. Its Choi operator is

$$
J_4=\frac13\sum_{a,s}(P_{a,s}^T)^{\otimes4}\otimes P_{a,s},
$$

a positive combination of product stabilizer projectors. Thus the map is an ordinary stabilizer instrument and satisfies the larger Choi-cone constraint. Retaining a measured input supplies the output; no extra pure output specimen is required.

## Exact conditional gain for every direction

For a fixed direction, the probability of a common sign in basis $a$ is $[(1+sru_a)/2]^4$. Let

$$
S_4=\sum_{a=x,y,z}u_a^4,\qquad \frac13\le S_4\le1.
$$

Expanding the two signs gives

$$
p_{\mathbf u}=\frac{3+6r^2+r^4S_4}{24}.
$$

The overlap of the conditional output Bloch vector with $\mathbf u$ is

$$
R_{\mathbf u}=\frac{4r(1+r^2S_4)}{3+6r^2+r^4S_4}.
$$

Since $F_{4,\mathbf u}=(1+R_{\mathbf u})/2$, the exact gain is

$$
F_{4,\mathbf u}-F_0
=\frac{r\left[1-6r^2+(4r^2-r^4)S_4\right]}
{2(3+6r^2+r^4S_4)}.
$$

The fidelity increases with $S_4$: its derivative is $2r^3(3+5r^2)/(3+6r^2+r^4S_4)^2>0$. The worst directions therefore have equal absolute Cartesian components, with $S_4=1/3$. Their gain is

$$
\min_{\mathbf u}(F_{4,\mathbf u}-F_0)
=\frac{r(3-14r^2-r^4)}{2(9+18r^2+r^4)}.
$$

This is strictly positive precisely when $0<r<r_*$. At $r=r_*$ the body-diagonal directions have zero gain; above it they lose fidelity under this particular filter. The success formula also gives $p_{\mathbf u}\ge1/8$.

## Prescribing average success

The bare filter's Haar-average success is

$$
p_0=\frac{1+2r^2+r^4/5}{8}.
$$

Fix $r\in(0,r_*)$ and a desired Haar-average success $p\in(0,1)$. If $p\le p_0$, retain a successful event with independent probability $p/p_0$. This changes the success rate without changing conditional fidelity.

If $p>p_0$, mix the filter with the channel $\mathcal I_1$ that returns one input and discards the other three:

$$
\mathcal E_\lambda=\lambda\mathcal E_4+(1-\lambda)\mathcal I_1,
\qquad
\lambda=\frac{1-p}{1-p_0}.
$$

This is a four-input ordinary stabilizer instrument. Its average success is $p$, and for every direction

$$
F_{\lambda,\mathbf u}-F_0
=\frac{\lambda p_{\mathbf u}(F_{4,\mathbf u}-F_0)}
{\lambda p_{\mathbf u}+1-\lambda}>0.
$$

The mixing probability may use the fixed noise parameter $r$. The prescribed quantity is average success; the direction-dependent success need not be constant. At $p=1$, $\lambda=0$ and the gain vanishes, consistently with the deterministic converse. No fidelity optimum at a prescribed success is asserted.

## Haar score and an exact example

For uniform directions, $\int S_4\,d\mathbf u=3/5$. Average the unnormalized accepted overlap before dividing by average success. The result is

$$
F_4^{\mathrm H}(r)
=\frac12+
\frac{2r/3+2r^3/5}{1+2r^2+r^4/5}.
$$

This accepted-data average improves on $F_0$ over the larger interval

$$
0<r<\sqrt{-3+\frac{4\sqrt6}{3}}\approx0.51574.
$$

That larger interval is a Haar-average statement. The guarantee for every direction remains $r<r_*$.

At $r=1/3$, the quantities are exact:

| Quantity | Value |
|---|---:|
| Raw input fidelity | 2/3 |
| Worst-direction conditional fidelity | 307/446 |
| Worst-direction conditional gain | 29/1338 |
| Minimum success | 223/1458 |
| Maximum success | 149/972 |
| Haar-average success | 62/405 |
| Accepted-data Haar fidelity | 43/62 |

These rational values supply a feasible witness without an optimization solver.

## Deterministic five-copy operation

Run the four-copy filter on the first four inputs. On success, return its accepted output. On failure, return the untouched fifth input. Conditional on a fixed direction, the fifth copy is independent of the first four, so rejection leaves it in the state $\rho_{\mathbf u}(r)$.

Every run now returns a qubit. The channel uses only stabilizer measurements and classical routing.

To define it on arbitrary five-qubit inputs, let $\mathbf s\in\{-1,1\}^4$ be a measurement pattern and put

$$
\Pi_{a,\mathbf s}=\left(\bigotimes_{i=1}^4P_{a,s_i}\right)\otimes I_5.
$$

Let $\mathcal R_{\mathbf s}$ retain qubit 1 for a unanimous pattern and qubit 5 otherwise, tracing out all other systems and relabeling the retained one as the output. Then

$$
\mathcal G_5(A)=\frac13\sum_{a,\mathbf s}
\mathcal R_{\mathbf s}\!\left(\Pi_{a,\mathbf s}A\Pi_{a,\mathbf s}\right).
$$

Every branch is completely positive. For each axis the projectors form a complete measurement, and each retention map preserves the branch trace. Thus $\mathcal G_5$ is trace preserving on arbitrary inputs. On the stipulated independent-copy family its fidelity is

$$
F_{5,\mathbf u}
=p_{\mathbf u}F_{4,\mathbf u}+(1-p_{\mathbf u})F_0.
$$

Consequently,

$$
F_{5,\mathbf u}-F_0
=\frac{r\left[1-6r^2+(4r^2-r^4)S_4\right]}{48},
\qquad
\min_{\mathbf u}(F_{5,\mathbf u}-F_0)
=\frac{r(3-14r^2-r^4)}{144}.
$$

The gain is strict throughout the same pointwise interval. At $r=1/3$, its worst-direction value is $29/8748$. The [deterministic converse](deterministic-converse.md) proves that four inputs cannot achieve such an unconditional improvement, even in the larger Choi-cone class.

The [verification suite](../verification/README.md) checks the formulas against direct Kraus-map evaluation and verifies the accepted-map and trace-preserving constraints. The universal statements follow from the exact inequalities above.
