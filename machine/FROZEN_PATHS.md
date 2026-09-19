# Exact frozen-path guide

Asset names are those in [RELEASE_ASSETS.md](../release/RELEASE_ASSETS.md). Paths below are archive-relative; `::` means “open that ZIP, then locate this member,” not a filesystem command. All commands are run after fresh extraction in the specified root. Use [the wrapper](../REPRODUCE.md) to avoid manual nesting.

## Principal archive roots

| Asset | Root directory | Purpose |
|---|---|---|
| 01 final clean closure | `I3322_FINAL_CLEAN_EXACT_VALUE_CLOSURE/` | Final theorem and canonical dependency custody |
| 02 integrated hostile audit | `I3322_FINAL_INTEGRATED_HOSTILE_AUDIT/` | Integration validation |
| 03 source-provenance audit | `I3322_PROJECT_SOURCE_PROVENANCE_AUDIT/` | External-premise and provenance validation |
| Public paper v0.1.2 | `I3322_PAPER_V0_1_2/` | Metadata/declaration successor; exposition and byte-preserved original replay wrapper |
| 06 rejected Sol proof | `build/I3322_O6_CLEAN_RECERTIFICATION/` | REJECTED — NOT THEOREM AUTHORITY |
| 07 rejecting audit | `I3322_O6_HOSTILE_AUDIT/` | Records the rejected branch's arithmetic failures |

The paper contains `reproducibility/I3322_PAPER_ASSEMBLY_INPUTS.zip`; its original wrapper verifies that archive, extracts its clean closure and audits, then follows the closure's canonical pins.

## Closure aliases

All six members below reside in the closure root's `inputs/` directory.

| Alias | ZIP filename |
|---|---|
| A | `01_CANONICAL_CLEAN_UPSTREAM_76d7.zip` |
| B | `02_O1_O5_CANONICAL_PROOF_b7fc.zip` |
| C | `03_O1_O5_HOSTILE_AUDIT_2bed.zip` |
| D | `04_O1_O5_PROVENANCE_SUPPLEMENT_09a8.zip` |
| E | `05_O6_SURVIVOR_PROOF_106ad.zip` |
| F | `06_O6_FINAL_AUDIT_CONSOLIDATION_18a9.zip` |

| Component | Extracted root and load-bearing sources | Exact replay command from that root |
|---|---|---|
| A | `I3322_CLEAN_UPSTREAM_HANDOFF/`; `CLEAN_UPSTREAM_INTERFACE.md` | No separate top-level replay; enter R0/R1 below |
| R0 inside A | `R0_CANONICAL/I3322_PHASE_B_R0.zip` → `I3322_PHASE_B_R0/`; `PROOF.md` | `python replay_all.py` |
| R1 inside A | `R1_CANONICAL/I3322_PHASE_B_R1.zip` → `I3322_PHASE_B_R1/`; `PROOF.md`, `NORMALIZATION.md`, `src/lower.py`, `src/upper.py` | `python replay_all.py` |
| B | `I3322_O1_O5_CANONICAL_PROOF/`; `DEFINITIONS.md`, `O1_O5_THEOREM.md`, `O1_PARAMETER_DOMAIN.md`, `O2_LOCAL_TAILS.md`, `O3_MATCHING_SOUNDNESS.md`, `O4_CARRIER_COMPLETENESS.md`, `O5_MATCH_EXISTENCE.md` | `python replay_all.py` |
| C | `I3322_O1_O5_HOSTILE_AUDIT/`; `AUDIT_VERDICT.md` | Historical validation; no new replay command prescribed here |
| D | `I3322_O1_O5_PROVENANCE_SUPPLEMENT/`; `PROVENANCE_VERDICT.md`, `VERDICT_UPDATE.md` | D001 closure record |
| E | `I3322_O6_CLEAN_RECERTIFICATION/`; `PROOF.md`, analytic Markdown arguments, `src/`, `certificates/` | `python replay_all.py --work-directory ../o6-generated` |
| F | `I3322_O6_FINAL_AUDIT_CONSOLIDATION/`; `FINAL_O6_AUDIT_VERDICT.md`, `REMAINING_FINDINGS.md` | Historical arithmetic/status consolidation |
| Final closure | `I3322_FINAL_CLEAN_EXACT_VALUE_CLOSURE/`; `FINAL_THEOREM.md`, `COMPONENT_INTERFACES.md`, `CLAIMS.json`, O7/O8 Markdown proofs | `python replay_all.py`; `python audit_integration.py` |

E's consumed conditional interface is in `inputs/I3322_O6_CLEAN_PORT_HANDOFF.zip::I3322_O6_CLEAN_PORT_HANDOFF/O1_O5_INTERFACE.md` and `DEFINITIONS.md`. B's definitions are semantically compared against these; different prose is not claimed byte-identical. The canonical upstream copies are byte-identical.

E certificate locators used by the audit guide include `certificates/phase_geometry.json`, `certificates/full_cover.json`, `certificates/central_monotonicity.json`, `certificates/scalar.json` and `certificates/root.json`. Degree-specific receipt filenames and exact source mapping are in its manifest and manuscript Appendix D.

The frozen Coladangelo source is reached through A's R0 archive, `inputs/I3322_PHASE_B_R0_HANDOFF.zip`, under its `05_NON_DOUGLAS_SOURCES/` source tree. The source audit's `COLADANGELO_AUDIT.md` and `WEB_SOURCE_LEDGER.md` identify the frozen version. No current internet content is required or imported by assembly.

Every replay work directory must be fresh and outside the corresponding sealed tree. Commands in the table require the identified assets; they are not commands for this curated `machine/` directory.
