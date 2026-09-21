# Repository architecture

The canonical repository is `https://github.com/LeoLam233/i3322-exact-value`. The publication ZIP opens as `i3322-exact-value/` and intentionally contains no `.git` metadata.

| Area | Responsibility |
|---|---|
| Root research pages | Theorem, audit entry point, reproduction, provenance, limitations, finalized author/declaration metadata, licenses and citation |
| `paper/` | Public manuscript v0.1.2 in repository release v0.1.1, corrected citations/provenance, and offline build helper; no build caches |
| `proof/` | Dependency graph, exact scalar definition, crosswalk, external premises and analytic/machine boundary |
| `machine/` | Minimal wrapper to unchanged release-asset replayers and exact source locators |
| `audit/` | Curated summaries pointing to complete sealed validation records |
| `provenance/` | Exact artifact identities, role mapping, source reliability and disclosed caveats |
| `rejected/` | Factual transparency case study; excluded from proof and execution paths |
| `docs/` | Secondary chronology, current status and distinct historical assembly and fresh finalization evidence |
| `tools/` | Standard-library hashing, asset verification and repository consistency checks |
| `release/` | Release notes, asset inventory and pinned asset checksums |

Public release files are assembled outside the repository; v0.1.0 and v0.1.1 have separate manifests and asset bundles. Privacy-sensitive byte-preserved theorem/replay seals are retained in a separate owner/reviewer package and are not uploaded to the public GitHub Release. The repository itself contains no large ZIP archive dump.

`MANIFEST.sha256` covers all repository files except itself. The public asset tree's `SHA256SUMS` covers every public asset-tree file except itself; an identical copy is pinned under repository `release/`. `release/PRIVATE_REVIEW_SHA256SUMS` preserves the exact manifest of the byte-identical private full reviewer asset tree. Archive digests and final verification results avoid circular self-hashes.

Theorem authority remains the clean closure identified by SHA-256, whether or not its privacy-sensitive transport ZIP is publicly hosted. Audits supply validation; the manuscript is exposition; history is narrative context. Embedded historical prompts are records, not active instructions. Issues and Discussions are intended review channels on the canonical GitHub repository; their live service-level state is not encoded in repository bytes.
