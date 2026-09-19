# Known source issues preserved

The frozen source-provenance audit reports **six source-text errors and zero load-bearing source errors**. Its overall verdict remains OPEN-MINOR. These are summaries of `SOURCE_ERRORS_AND_CAVEATS.md` in asset 03, not new corrections to the frozen sources.

| Finding | Frozen location and issue | Frozen disposition |
|---|---|---|
| SP-001 | Coladangelo v1 p.22, Lemma 6.2: a scalar shift cannot make every entry of a tridiagonal matrix positive | MINOR, non-load-bearing; existing irreducibility/zero-propagation and R0 arguments establish the weaker positive-eigenvector fact actually needed |
| SP-002 | p.19, Proposition 5.3: the unit-circle sentence repeats the cosine square | DOCUMENTATION, non-load-bearing; correct displayed blocks and internal reconstruction |
| SP-003 | p.27, equation (43): omitted trace-norm bars | DOCUMENTATION, non-load-bearing; the adjacent established norm inequality supplies the bound |
| SP-004 | p.23, Lemma 6.2: wrong equation reference (41) instead of local stationarity relations (29)–(30) | DOCUMENTATION, non-load-bearing |
| SP-005 | p.35, Lemma 7.7: the concave-envelope argument names condition (50) instead of pairwise condition (51) | DOCUMENTATION, non-load-bearing; the explicit summation uses the intended hypothesis |
| SP-006 | Frozen Mghirbi manuscript: printed lower decimal `.2508753845139766...` is inaccurate | MINOR, non-load-bearing; the exact rational lower value still strictly exceeds the frozen R1 threshold `.2508753845139765` |
| SP-007 | Complete pre-release candidate-generation ancestry is not authenticated | MINOR provenance limit; released byte identity and independent exact validity pass |
| SP-008 | Surviving O6 generic midpoint-helper defect M001 | MINOR software defect; genuine, unpatched, non-load-bearing on the submitted path |

SP-007 and SP-008 are distinct from the six source-text errors. The audit's four-minor/four-documentation accounting is preserved. Existing supporting arguments were located; no frozen theorem was repaired in this assembly.

The retained historical v0.1.1 paper package contains earlier v0.1 build notes whose “PDF not produced” statements describe an earlier assembly. Its later build receipt records the historical 33-page PDF. The current public v0.1.2 manuscript is a metadata/declaration successor with fresh successful build/render QA and unchanged mathematical content. The [paper guide](../paper/README.md) distinguishes these historical and current identities.
