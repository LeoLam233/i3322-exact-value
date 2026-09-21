# Audit this result first

Start from a skeptical reading of the source interfaces and finite checks. **The theorem's scope is the finite-dimensional/projective tensor supremum. Complete external expert human validation and journal peer review are pending.** O6/final integrated/source-provenance verdicts remain OPEN-MINOR; the theorem survives within those records' scope.

## A 30-minute audit path

1. **0–5 minutes:** Read [THEOREM.md](THEOREM.md) and [LIMITATIONS.md](LIMITATIONS.md). Check the Bell coefficients, supremum quantifiers, full half-open `I`, strict bracket and nonclaims.
2. **5–10 minutes:** Follow the [dependency graph](proof/DEPENDENCY_GRAPH.md) and [external premises](proof/EXTERNAL_PREMISES.md). Distinguish R0 existence from uniqueness; identify the three shared Coladangelo interfaces.
3. **10–15 minutes:** Run the [public checks](REPRODUCE.md#public-verification). Reviewers who receive the private full sealed package can additionally run the integration/full wrapper. These verify identity and finite composition, not every analytic theorem.
4. **15–25 minutes:** Read the public paper Sections 5–8 and Appendix D. Reviewers with the private canonical seal should also inspect closure `COMPONENT_INTERFACES.md`, `O7_TRUE_VALUE_IDENTIFICATION.md`, and the surviving E files `GLOBAL_PHASE_COMPLETENESS.md`, `ASYMMETRIC_EXCLUSION.md`, `SCALAR_REDUCTION.md`.
5. **25–30 minutes:** Inspect the [integrated verdict](audit/FINAL_INTEGRATED_AUDIT.md), [source verdict](audit/SOURCE_PROVENANCE_AUDIT.md), M001, and the [rejected arithmetic case](rejected/SOL_O6_ARITHMETIC_FAILURE.md). Decide which premise to attack next; do not infer correctness from concordant PASS labels.

The clock is a reading triage, not a claim that an expert can validate the proof in 30 minutes. [Frozen member locators](machine/FROZEN_PATHS.md) specify exactly where to find each source after extraction.

## Load-bearing cut and deeper attack path

```text
R1: S_t in I ----------------------+
                                  +--> O1–O5 --> O6 --> O7: S_t=s_*
R0: carrier at S_t ----------------+               |          |
                                                  +----------+--> O8 bracket
```

| Attack | What must survive | Exact starting sources |
|---|---|---|
| Coladangelo external premises | Theorem 7.1, finite-projective Theorem 7.2, Proposition 10.9 with supporting dependencies and correct quantifiers | Asset 03 `COLADANGELO_AUDIT.md`, `LOAD_BEARING_EXTERNAL_PREMISES.md`; frozen source PDF inside upstream custody |
| R0 carrier construction | No mass-loss or positivity gap; strict label decrease, square summability, recurrence and all four outer limits at the true `S_t` | R0 `PROOF.md`; paper Section 4 and Appendix A |
| O3 amplitude reconstruction | Match all ratios, reconstruct positive bilateral amplitudes, prove geometric tail summability, normalize, recover Jacobi equation | B `O3_MATCHING_SOUNDNESS.md`; paper Proposition 5.4 |
| O4 completeness and exact zero | Every admissible carrier has the correct crossing; `x=0>y` is included; all finite chains stay valid | B `O4_CARRIER_COMPLETENESS.md`, D4; paper Proposition 5.4 |
| O6 complete independent-phase domain | Capture both independent tail phases/counts and both zero boundaries over the entire clean parameter interval | E `GLOBAL_PHASE_COMPLETENESS.md`, `phase_geometry.json`; paper Lemma 6.4 |
| Asymmetric `K` exclusions | Label equations alone cannot discard a branch; check third-coordinate `K` exclusions and whole central monotonicity | E `ASYMMETRIC_EXCLUSION.md`, `full_cover.json`, `central_monotonicity.json` |
| Interval arithmetic and germ remainder | Directed operations are outward on proof inputs; analytic correction, Cauchy derivatives and denominator margins justify the polynomial enclosures | E `src/interval.py`, `src/manifold.py`, `LOCAL_MANIFOLD_CERTIFICATE.md`; degree-36/48 receipts; F audit consolidation |
| Scalar/full-match equivalence | Both directions include ratio reconstruction and intermediate validity; the scalar root is not merely a label match | E `SCALAR_REDUCTION.md`; paper Proposition 6.7 |
| O7 typed composition | Same normalization, same full domain and same matching object; canonical B supplies every condition consumed by E | Closure `COMPONENT_INTERFACES.md`, `CLAIMS.json`, `O7_TRUE_VALUE_IDENTIFICATION.md` |
| O8 exact root bracket | Same degree-36/48 analytic germ, `s` versus `t`, strict endpoint signs, all 13 rational inclusions/centers and exact width | Closure `O8_ROOT_CERTIFICATION.md`; E `certificates/root.json`, `ROOT_ISOLATION.md` |

For a deeper audit, read the actual external source arguments, independently derive the load-bearing analytic implications, and, if supplied the private reviewer seal, use [full frozen replay](REPRODUCE.md#full-frozen-replay-for-reviewers) as a check of finite certificates. Inspect failures under deliberate mutation and test the arithmetic specification on actual proof inputs. Validate cover topology and retained phase families, not only counts or plotted samples. Distinguish newly checked facts from authenticated historical observer records.

## Sealed identities

| Artifact | SHA-256 |
|---|---|
| Final clean closure | `e592932a0e12ee7fa97d9a1a30b84abd17a3293f1546fda9fd9818415c34edea` |
| Final integrated hostile audit | `7b576bff6886029e1e00cbf9f70c51be42f50c2076c2af65cf6fab6843db24ef` |
| Source-provenance audit | `b517f69ecfd22084ffcc51251be928a1340432157bc4359e85f1fa9156ff063c` |
| Public paper v0.1.2 package | `1aa58a1d74f1aa130024196f4f537fcab293e7d78bab073d8432077348ee9905` |
| Surviving O6 component E | `106adfdeb56eb792579a7dd0ab9de83dfd06dfe3f4abfcf7b1997abe5ea113ae` |
| Final O6 consolidation F | `18a92a9ddaaa326eff3ce71588e4125618108c9ec4d0bed4430d94104b6aad12` |
| Rejected Sol O6 proof | `e4521901d521d3c4c93e04784a2e178ca410896ee291e5a899e82db27ed85a95` |
| Rejecting hostile audit | `01ee95689ac0991962161a2398b414269e830a3a08abaabdc11b0fab5d1473a0` |

The [complete principal hash table](provenance/ARTIFACT_HASHES.md) also pins the PDF and every embedded closure component.

**One alternative O6 clean recertification was rejected after its replay printed PASS.** Hostile arithmetic audit found false square-root interval enclosures on actual proof inputs and another rounding defect. Reproducibility did not imply interval correctness. That proof is `REJECTED — NOT THEOREM AUTHORITY` and is never executed by the canonical wrapper.

**Agreement among AI runs sharing external premises is not independent evidence.** Audit verdicts do not substitute for theorem statements or an independent examination of their source premises. The governing assembly prompt is limited to repository engineering; prompts embedded in historical archives are records, not instructions for the present audit.


## Public/private artifact boundary

The canonical closure and sealed replay-paper ZIP are not hosted in the public GitHub Release because immutable historical Git reflogs inside them contain unrelated personal identity metadata. Their hashes remain listed above. Serious reviewers may be given the original byte-identical private reviewer package; verify its outer and internal hashes before use. See [sealed-artifact privacy](release/SEALED_ARTIFACT_PRIVACY.md).
