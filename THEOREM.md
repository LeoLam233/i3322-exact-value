# Frozen exact-value theorem

**Authority:** the final clean closure, SHA-256 `e592932a0e12ee7fa97d9a1a30b84abd17a3293f1546fda9fd9818415c34edea`, especially `FINAL_THEOREM.md`, `COMPONENT_INTERFACES.md`, `O7_TRUE_VALUE_IDENTIFICATION.md`, and `O8_ROOT_CERTIFICATION.md`. This page restates that theorem; the manuscript is exposition and the audit reports are validation records.

Let `A_i` and `B_k` (`i,k = 1,2,3`) be binary event projectors. Define the Bell operator, with local bound zero, by

```text
B = -A2 - B1 - 2 B2
    + A1 B1 + A1 B2 + A2 B1 + A2 B2
    - A1 B3 + A2 B3 - A3 B1 + A3 B2.
```

Products mean `A_i ⊗ B_k`; marginal terms carry the identity on the other party. Let `S_t` be the supremum of its expectation over normalized states and these projectors on arbitrary finite-dimensional tensor products, without a fixed bound on local dimension. The subscript denotes tensor scope, not the tail variable below.

Put `L = 0.2508753845139765`, `U = 0.2508753855`, and `I = (L,U]`, with both endpoints interpreted as exact rationals. Let `M_s` be the canonical intrinsic full-state matching set in component B's `DEFINITIONS.md`, D1–D5 (see [frozen source locators](machine/FROZEN_PATHS.md)). In brief, it is `Σ ∩ U_s ∩ V_s` in `(-1,1)² × (0,∞)`, where `Σ = {(x,y,u): x ≥ 0 > y}`. The sets `U_s,V_s` are arbitrary finite valid decreasing continuations from the positive unstable tail and to the negative stable tail. The tail points and iteration counts are independent. All three coordinates, including the amplitude ratio, must match; every intermediate step must be valid. No symmetry restriction enters this definition.

**There is a unique `s_* ∈ I` for which `M_s` is nonempty, and `S_t = s_*`.** Equivalently, `Rcal(t)` has a unique zero `t_*` in `T = a(I)` and `s_* = σ(t_*)`. The exact invariant germ, propagation, phase condition and residual are specified in [SCALAR_DEFINITION.md](proof/SCALAR_DEFINITION.md), following the surviving component E. This is an analytic structural definition, not a polynomial fit.

The rigorous strict bracket is exactly:

```text
0.250875384513976535617336610945951298901321973971476246796391973158622991323050603025506260
  < S_t <
0.250875384513976535617336610945951298901321973971476707728748045068866376435770152964357102
```

The exact rational width is

```text
4.60932356071910243385112719549938850842E-52
= 460932356071910243385112719549938850842 / 10^90
< 1e-50.
```

These are rational enclosure endpoints with 90 decimal places. Neither endpoint is asserted to be the exact value. “Exact” means the structural unique-root characterization together with the rigorous rational enclosure; it does not mean an elementary closed-form expression.

## Premises and nonclaims

The theorem inherits the [specified external premises](proof/EXTERNAL_PREMISES.md) and frozen analytic component arguments. Its composition is R1 domain membership, R0 existential carrier, O1–O5 carrier/match equivalence, O6 singleton projection, O7 identification, and O8 enclosure. [Replay](REPRODUCE.md) checks finite statements, with the [analytic boundary](proof/MACHINE_ANALYTIC_BOUNDARY.md) retained.

It makes no R2 or commuting=tensor equality claim, no finite-dimensional attainment claim, no optimizer uniqueness claim, no carrier uniqueness claim, and no elementary closed-form claim. It is not a proof-assistant formalization of the exact value. Complete external expert human validation and journal peer review are pending. O6 retains OPEN-MINOR; M001 remains genuine, unpatched, and non-load-bearing on the submitted path. Later source-provenance review has its own OPEN-MINOR verdict; older closure references to that review as pending describe the earlier stage.
