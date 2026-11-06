# Related work and scope

## Contribution and conventions

We study an unknown pure qubit $\psi_{\mathbf u}=(I+\mathbf u\cdot\sigma)/2$ observed through independent depolarization,
$$
\rho_{\mathbf u}(r)=\frac{I+r\mathbf u\cdot\sigma}{2},\qquad 0<r<1.
$$
The target fidelity is the overlap with $\psi_{\mathbf u}$, and the raw benchmark is $(1+r)/2$. For a heralded map, the Haar figure of merit is the ratio of the averaged unnormalized overlap to the averaged success. We also give a stronger construction that improves the conditional fidelity for every direction separately.

The main result is a copy-resource boundary: **four copies are necessary and sufficient for the existence of heralded gain, and five for deterministic gain**. Necessity holds over the stabilizer Choi cone; sufficiency uses ordinary Pauli measurements, classical randomness, and a spare input on failure. These are thresholds for the existence of a nonempty noise interval. They are not a characterization at every $r$, nor an exact fidelity/yield frontier. Within the interval of pointwise gain, independent thinning or mixing with a return-one-input channel achieves strict pointwise gain at every prescribed Haar-average success probability $p\in(0,1)$. At $p=1$, full rank of the average input forces a trace-nonincreasing map to be trace-preserving, so the four-copy deterministic obstruction applies.

## Estimation with abstention: the inherited construction

Bernat Gendra, Elio Ronco-Bonvehi, John Calsamiglia, Ramon Muñoz-Tapia, and Emilio Bagan studied estimation of an unknown pure-qubit direction from independently depolarized copies with an abstention option. Their equation (22) evaluates fidelity on accepted data. At the end of §3.2, they explicitly describe measuring every spin along a fixed axis and abstaining unless all outcomes agree. [1]

Our fixed-axis unanimity map is this known construction, with the guessed Pauli eigenstate retained as a quantum output. Its Haar conditional performance is consequently inherited, not a new purification mechanism. The three-axis Pauli randomization provides a pointwise refinement: for a sufficiently noisy input, every direction improves, including directions orthogonal to any individual measurement axis.

The fixed-axis protocol alone has no such guarantee: equatorial directions relative to that axis have fidelity $1/2$ on acceptance. This distinction matters because a large accepted-data average can partly reflect which inputs succeed. The pointwise construction and the deterministic fallback avoid relying only on that selection effect.

Gendra et al. optimize estimation, with a classical guessed direction or an equivalent prepared output. They do not supply the converse for all coherent maps in the stabilizer Choi cone. The three-copy heralded impossibility and four-copy deterministic impossibility are the substantive ingredients behind our exact thresholds.

## Completely stabilizer-preserving channels

Seddon and Campbell characterize completely stabilizer-preserving channels by their Choi states in Theorem 3.1. [5] That representation is inherited. The present converses use its subnormalized version with unequal input and output sizes; the Bell-projection argument in the heralded proof states the required extension explicitly. The new inequalities constrain this larger class, while the matching constructions are ordinary stabilizer instruments.

## He et al.: two-copy no-go and multi-copy numerical evidence

Keming He, Chengkai Zhu, Hongshun Yao, Jinguo Liu, Yinan Li, and Xin Wang prove that classically simulable free operations cannot improve the universal two-copy purification fidelity under depolarization. Their qubit free class is expressed through the completely stabilizer-preserving Choi constraint. Their final PRL abstract also reports numerical extensions to three and four copies. [2]

The accessible arXiv v2 uses the same $\delta=1-r$ noise convention and the same success-weighted Haar fidelity as our comparison. Its equations (2)–(3) fix average success, and Appendix proposition S2 expresses positivity, trace-nonincreasing behavior, and nonnegative stabilizer-cone decomposition. The explicit four-copy filter satisfies these constraints. For example, at $r=1/3$ it has average success $62/405$ and conditional Haar fidelity $43/62>2/3$. Pauli randomization additionally yields strict gain for every input direction.

Our result leaves the proved two-copy theorem intact and establishes a three-copy qubit converse analytically. The four-copy heralded witness is incompatible with the all-noise/all-success numerical impossibility summarized by arXiv v2 Table 1. The deterministic four-copy converse explains why the distinction between heralded and certain-success protocols is essential.

The public code must be described carefully. At commit `b50cb1dba98399a1ea8b2ae3cb6bcacd69643ce0`, the universal qubit depolarizing script is configured for $n=2$, $\delta=0.5$, $p=0.5$, using the three-qubit stabilizer matrix. We inspected its constraints and independently evaluated our witnesses in the corresponding Haar objective. We did not run its MATLAB/CVX solver, locate a documented three/four-copy run, or establish the cause of the reported numerical conclusion. [3]

For the four-input version of the stated constraints at $\delta=p=1/2$, mixing the filter with the return-one channel gives the exact accepted-data Haar witness

$$
F=\frac34+\frac5{6228}>\frac34.
$$

This example uses $r=1/2$ and concerns Haar fidelity. The guarantee for every direction uses the smaller interval in the main theorem. The [direct matrix check](../verification/check_published_sdp_witness.py) evaluates the feasible Choi operators without an optimization solver.

The detailed model comparison uses arXiv v2. The final APS abstract was inspected, but the final PDF and supplement were unavailable through the access used for this project. We do not assume that every preprint equation or table is unchanged in the version of record.

## The later two-copy resource law

He, Enji Xiong, and Wang's “A Nonstabilizerness Resource Law for Universal Quantum State Purification” explicitly studies the cost of fidelity improvement from **two input copies**, in its model. [4] A resource law at fixed copy number two is compatible with our result: increasing the number of noisy inputs changes the available resource tradeoff. Our construction shows that nonstabilizer operations are unnecessary for a limited universal fidelity improvement once the relevant copy threshold is reached.

Its two-input resource laws and the present copy thresholds address different available input budgets.

## References

1. B. Gendra, E. Ronco-Bonvehi, J. Calsamiglia, R. Muñoz-Tapia, and E. Bagan, **Beating noise with abstention in state estimation**, *New Journal of Physics* **14**, 105015 (2012). [DOI](https://doi.org/10.1088/1367-2630/14/10/105015); [arXiv:1205.5479](https://arxiv.org/abs/1205.5479); [inspected PDF](https://arxiv.org/pdf/1205.5479). Fixed-axis protocol: p. 10, end of §3.2; accepted-data metric: equation (22).

2. K. He, C. Zhu, H. Yao, J. Liu, Y. Li, and X. Wang, **No-Go Theorems for Universal Quantum State Purification via Classically Simulable Operations**, *Physical Review Letters* **136**, 090204 (2026). [DOI and final abstract](https://doi.org/10.1103/bdw8-k91v); [arXiv:2504.10516v2](https://arxiv.org/html/2504.10516v2). Full-text comparison in this project refers to the identified arXiv version.

3. QuAIR, **NonMagic-Purification-codes**, inspected at [commit b50cb1dba98399a1ea8b2ae3cb6bcacd69643ce0](https://github.com/QuAIR/NonMagic-Purification-codes/tree/b50cb1dba98399a1ea8b2ae3cb6bcacd69643ce0). [Universal qubit depolarizing script](https://github.com/QuAIR/NonMagic-Purification-codes/blob/b50cb1dba98399a1ea8b2ae3cb6bcacd69643ce0/Non_magic_purification/universal_cspo_purification_depo_noise.m), blob `0826ded38b0b2dff29a40768b90ba1fa2dd38101`.

4. K. He, E. Xiong, and X. Wang, **A Nonstabilizerness Resource Law for Universal Quantum State Purification**, arXiv:2607.08626 (2026). [Abstract](https://arxiv.org/abs/2607.08626); [full preprint](https://arxiv.org/html/2607.08626v1). Scope comparison uses its introduction and two-input model.

5. J. R. Seddon and E. T. Campbell, **Quantifying magic for multi-qubit operations**, *Proceedings of the Royal Society A* **475**, 20190251 (2019). [DOI](https://doi.org/10.1098/rspa.2019.0251); [arXiv:1901.03322v2](https://arxiv.org/abs/1901.03322v2). Channel Choi characterization: Theorem 3.1.
