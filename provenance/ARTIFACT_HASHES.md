# Authenticated artifact identities

The sole public-finalization input was `I3322_PUBLIC_RELEASE_FINALIZATION_INPUTS.zip`, SHA-256 `c85cca86fa8c3c87de0cab88eec5ec537817d716898760b35a7bff9f4aa46512`. All seven INPUT_MANIFEST.sha256 entries were verified after fresh extraction. Its repository ZIP is `f3dff1f56d62a9afc048c8a583953353aeac8ef09525811d66d047671e895d05` and release-assets ZIP is `862366ecf42fc1b26dd6e9d584e94e20dd0fc2d3e1e0338e975acc3a11079ef2`. No outside project-specific material was used.

## Principal authenticated artifacts

| File | Role | SHA-256 |
|---|---|---|
| `01_FINAL_CLEAN_EXACT_VALUE_CLOSURE_e592.zip` | CANONICAL theorem authority; private reviewer seal | `e592932a0e12ee7fa97d9a1a30b84abd17a3293f1546fda9fd9818415c34edea` |
| `02_FINAL_INTEGRATED_HOSTILE_AUDIT_7b57.zip` | OPEN-MINOR; theorem survives (validation) | `7b576bff6886029e1e00cbf9f70c51be42f50c2076c2af65cf6fab6843db24ef` |
| `03_PROJECT_SOURCE_PROVENANCE_AUDIT_b517.zip` | OPEN-MINOR; theorem source-provenance survives (validation) | `b517f69ecfd22084ffcc51251be928a1340432157bc4359e85f1fa9156ff063c` |
| `I3322_PAPER_V0_1_2.zip` | Sealed v0.1.2 replay carrier; privacy-withheld from public Release | `1aa58a1d74f1aa130024196f4f537fcab293e7d78bab073d8432077348ee9905` |
| `paper_v0_1_2.pdf` (v0.1.0 release) | Original public v0.1.2 33-page manuscript; historical release identity | `81b75cd3a720ab0e2953bdbd79f70c969af5fc48ab01caa75f4522b229f51f2f` |
| `paper_v0_1_2.pdf` (v0.1.1 release) | Final corrected public 35-page manuscript; exposition, not theorem authority | `8c96ffe8925e2c037ee6837de7e83f1b9bb0e8ff4714ff785a99eb594a2f3f8b` |
| `06_REJECTED_SOL_O6_PROOF_e452.zip` | REJECTED — NOT THEOREM AUTHORITY | `e4521901d521d3c4c93e04784a2e178ca410896ee291e5a899e82db27ed85a95` |
| `07_REJECTED_SOL_O6_HOSTILE_AUDIT_01ee.zip` | Rejecting hostile audit (historical validation) | `01ee95689ac0991962161a2398b414269e830a3a08abaabdc11b0fab5d1473a0` |

All authenticated mathematical/validation/rejected-branch seals remain byte-identical. Public hosting is narrower than artifact authority: the canonical closure and replay-paper ZIP are privacy-withheld from the GitHub Release, while their SHA-256 identities remain public. The PDF/readable source are public exposition; the rejected branch remains outside canonical replay.

## Historical manuscript identities

| Historical file | SHA-256 |
|---|---|
| `historical/04_PAPER_V0_1_1_0ea5.zip` | `0ea54751e6209b64ff7957363195c1511b442d4fb2dd823421046ba85a09d0a0` |
| `historical/05_paper_v0_1_1_c1a6.pdf` | `c1a6e364425a61ca8bae4e94cdf50e81f1a11b9ba3373e481747050e2b426bd0` |

Both historical identities are retained byte-for-byte for custody/build-QA provenance, not as the current public paper. The historical ZIP is privacy-withheld from public hosting. The prior repository-assembly input identity is retained in the machine-readable index as historical provenance.

## Embedded canonical closure components

These remain inside asset 01 under `I3322_FINAL_CLEAN_EXACT_VALUE_CLOSURE/inputs/`; they are not loose repository binaries.

| Component | SHA-256 |
|---|---|
| A: `01_CANONICAL_CLEAN_UPSTREAM_76d7.zip` | `76d7f205d494d09c791d4a862794b6ef5603cc02c494bddf0efb4368ad7ec052` |
| B: `02_O1_O5_CANONICAL_PROOF_b7fc.zip` | `b7fc43c9f2ad219235e6dfe6d63fe8030f308cb1b6ad56263d2f91283d86989f` |
| C: `03_O1_O5_HOSTILE_AUDIT_2bed.zip` | `2bed5d0e22efe931061e0b989282b4cb0eaef2629cf6d8b691a160274b29715b` |
| D: `04_O1_O5_PROVENANCE_SUPPLEMENT_09a8.zip` | `09a8c45a9738f2fedf1871c62d15516ff81d21f2b98a3e28e272caa864224832` |
| E: `05_O6_SURVIVOR_PROOF_106ad.zip` | `106adfdeb56eb792579a7dd0ab9de83dfd06dfe3f4abfcf7b1997abe5ea113ae` |
| F: `06_O6_FINAL_AUDIT_CONSOLIDATION_18a9.zip` | `18a92a9ddaaa326eff3ce71588e4125618108c9ec4d0bed4430d94104b6aad12` |

Surviving E `certificates/root.json` has SHA-256 `6a0154a67ec857c2565dd5036745cd591658f6dea668b6cb3d03f84d8b062117`. The theorem's displayed decimal strings were read from its `s_enclosure` field and checked against the frozen closure and paper source.

The privacy-filtered public GitHub Release is hashed in [release/SHA256SUMS](../release/SHA256SUMS). The original full reviewer asset tree is pinned separately in [release/PRIVATE_REVIEW_SHA256SUMS](../release/PRIVATE_REVIEW_SHA256SUMS), and its outer ZIP SHA-256 is recorded in [sealed-artifact privacy](../release/SEALED_ARTIFACT_PRIVACY.md). The machine-readable role/hash index is [artifact_index.json](artifact_index.json). A manifest is an integrity mechanism, not mathematical authority.
