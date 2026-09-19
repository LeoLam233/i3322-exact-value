# Sealed-artifact privacy boundary

The canonical theorem and replay chain was originally sealed before public-release packaging. A recursive pre-publication scan later found an unrelated historical **personal email address** and a superseded local Git identity inside Git reflogs nested in a frozen checkout of the Pauwels source repository.

Those reflogs are historical transport/provenance metadata, not mathematical premises. Editing or deleting them inside the canonical archives would change the byte identities and break the previously audited custody chain. Therefore v0.1.0 uses the following policy:

- the readable repository and public PDF are published normally;
- public release assets contain only archives/files that passed the privacy sweep for this personal email identity;
- affected frozen archives are **withheld from the public GitHub Release** and retained byte-for-byte in a private full reviewer package;
- their canonical SHA-256 identities remain published so reviewers can bind a privately supplied archive to the recorded theorem/audit chain;
- no theorem, proof, certificate, source-premise statement or audit verdict is modified by this privacy boundary.

## Withheld byte-identical artifacts

| Artifact | SHA-256 | Reason for withholding from public Release |
|---|---|---|
| `01_FINAL_CLEAN_EXACT_VALUE_CLOSURE_e592.zip` | `e592932a0e12ee7fa97d9a1a30b84abd17a3293f1546fda9fd9818415c34edea` | contains nested historical Git reflogs with personal identity metadata |
| `I3322_PAPER_V0_1_2.zip` | `1aa58a1d74f1aa130024196f4f537fcab293e7d78bab073d8432077348ee9905` | embeds the canonical closure/reproducibility archive |
| `historical/04_PAPER_V0_1_1_0ea5.zip` | `0ea54751e6209b64ff7957363195c1511b442d4fb2dd823421046ba85a09d0a0` | embeds the same frozen provenance chain |
| `I3322_FULL_AUDIT_BUNDLE_v0.1.zip` | `9c71431df5b7e7c1c34390b60b807453da43f8c93c0b2f5043a950ebcd9954df` | contains the canonical closure and replay-paper package |

The private full reviewer asset ZIP produced by the earlier offline finalization is preserved unchanged with outer SHA-256 `93ac17e3d1471a8d74f5f88f9029b9852c2d221f70b13ecd6fb00bc606d28598`.

A reviewer who receives that private package should verify both its outer digest and `release/PRIVATE_REVIEW_SHA256SUMS` before using it for full frozen replay.
