# Frozen obligation to manuscript crosswalk

Numbers below use the shared section theorem counter in main.tex and were
checked in the sealed paper package by its tools/check_manuscript.py. Appendix D repeats the crosswalk with
LaTeX references, so it will track the compiled numbering.

| Frozen item | Manuscript result | Exact source and role |
|---|---|---|
| Normalization | Definition 2.1; Proposition 2.2 | A:CLEAN_UPSTREAM_INTERFACE.md; R1:NORMALIZATION.md. Finite projective tensor supremum, event labels, involution conversion. |
| R1 | Proposition 3.1; Appendix B | R1:PROOF.md §§1–4; src/lower.py and src/upper.py. Explicit finite strategy and uniform positive word identity give L < S_t <= U. |
| External analytic interfaces | External premise 3.2 | Coladangelo v1 Theorem 7.1, finite-projective tensor clause of Theorem 7.2, Proposition 10.9. Stated narrowly; shared ancestry retained. |
| Finite realization | Proposition 3.3; Appendix A.1 | R0:PROOF.md §§1–2. q*=S_t and universal Jacobi comparison, by finite realizations and continuity. |
| R0 | Theorem 4.2; Appendix A | R0:PROOF.md §§3–14. Positive normalized strictly decreasing bilateral carrier; full ratio and outer label limits. |
| O1 | Proposition 3.1; Section 5, domain equations | B:DEFINITIONS.md D1 and O1_PARAMETER_DOMAIN.md. Whole I=(L,U] and T=a(I), not the final narrow bracket. |
| O2 | External premise 5.1; Lemma 5.2; neighborhood-independence paragraph | B:O2_LOCAL_TAILS.md; O1_O5_THEOREM.md items 1–2. Hyperbolicity, analytic local tails and convergent-tail capture. |
| O3 | Proposition 5.4, soundness direction | B:O3_MATCHING_SOUNDNESS.md. All three coordinates, geometric square summability, positive amplitude reconstruction, Jacobi equation. |
| O4 | Proposition 5.4, completeness direction | B:O4_CARRIER_COMPLETENESS.md. Arbitrary admissible carrier, unique crossing including x=0, actual valid finite chains. |
| O5 | Proposition 5.5 | B:O5_MATCH_EXISTENCE.md. Instantiate R1 and existential R0 in the bridge to get a true-value match. |
| O6 algebra | Lemma 6.1 and Appendix C | E:SYMBOLIC_DERIVATION.md; src/exact.py. Canonical conjugacy, reverser, contact structure and 48 identities. |
| O6 analytic germ | Certificate 6.2 and its proof | E:LOCAL_MANIFOLD_CERTIFICATE.md; src/manifold.py; degree-36 and degree-48 receipts. Actual analytic function and rigorous derivatives. |
| O6 domain completeness | Certificate 6.3; Lemma 6.4 | E:GLOBAL_PHASE_COMPLETENESS.md; phase_geometry.json. All independent phases and exact-zero boundaries enter the closed envelope. |
| O6 asymmetric exclusion | Certificate 6.5; Proposition 6.6 | E:ASYMMETRIC_EXCLUSION.md; full_cover.json and central_monotonicity.json. Projected inverse, all full-match residuals, whole central monotonicity. |
| O6 scalar and uniqueness | Proposition 6.7; Certificate 6.8; Theorem 6.9 | E:SCALAR_REDUCTION.md and GLOBAL_UNIQUENESS.md. Scalar zero iff intrinsic full match, strict derivative on full interval, fresh endpoint existence signs. |
| O7 | Theorem 7.1 | Closure:O7_TRUE_VALUE_IDENTIFICATION.md and COMPONENT_INTERFACES.md. S_t belongs to the singleton parameter projection. |
| O8 | Theorem 8.1 | Closure:O8_ROOT_CERTIFICATION.md; E:ROOT_ISOLATION.md; E:certificates/root.json. Same germ, 13 rational Newton inclusions, strict signs and exact width. |
| Source/audit boundaries | Sections 9–11; Appendix E | Final integrated audit and project source-provenance audit. Confidence/status evidence, not substitute mathematical premises. |

A–F are the six inputs embedded in the final closure, as explained in
Appendix D and the sealed paper REPRODUCIBILITY.md; see [frozen paths](../machine/FROZEN_PATHS.md). R0 and R1 are inside A. E is only the
surviving Astra component with SHA-256
106adfdeb56eb792579a7dd0ab9de83dfd06dfe3f4abfcf7b1997abe5ea113ae.
The rejected Sol O6 branch and historical Astra/Douglas proof material are
not used.

Semantic interface compatibility is represented by the same definitions in
the manuscript. The frozen upstream copies are byte-identical; differently
worded matching definitions are not falsely called byte-identical.
