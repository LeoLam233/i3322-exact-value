# Public manuscript v0.1.2 in repository release v0.1.1

[Read the PDF](paper_v0_1_2.pdf). Corrected-release PDF SHA-256: `af355a052b3a7377ff668291b59b1dc1b2ca4619e94f9d12a3f21e38387a5c57`.

The original sealed replay package `I3322_PAPER_V0_1_2.zip` has SHA-256 `1aa58a1d74f1aa130024196f4f537fcab293e7d78bab073d8432077348ee9905`. It contains the pre-correction LaTeX/BibTeX source, PDF, build/render QA, replay wrapper and byte-preserved reproducibility archive. Because that embedded frozen provenance chain contains historical personal-email metadata in Git reflogs, the sealed replay package is retained privately rather than uploaded to the public GitHub Release. It is preserved unchanged as historical build/replay provenance. The readable source tree and rebuilt `paper_v0_1_2.pdf` are the current public manuscript surfaces.

The pre-existing manuscript edition number remains v0.1.2 because v0.1.1 was already used in the preserved pre-publication manuscript/build-QA history. The title page identifies repository release v0.1.1 explicitly. This corrective release adds the missing Douglas citations and historical/priority explanation in the introduction, matching section and provenance section. **MATHEMATICAL CLAIM OR PROOF CODE CHANGED: NO.** No theorem statement, proof step, external-premise scope, audit caveat, exact numerical string or validation claim changed.

Author: Dehao Lin; School of Physics, Sun Yat-sen University, Guangzhou, China; lindh9@mail2.sysu.edu.cn. No ORCID is supplied and no AI system is an author. See [authorship](../AUTHORSHIP.md) and the unchanged [AI assistance disclosure](AI_ASSISTANCE_DISCLOSURE.md).

The corrective offline build exited 0 using Tectonic 0.17.0 (XeTeX), BibTeX and two automatic reruns. It has 35 pages, zero undefined references/citations, zero fatal LaTeX errors and one 1.59357 pt overfull hbox in unchanged Appendix B material. All 35 pages were rendered and visually reviewed without clipping, overlap or unreadable glyphs. The exact long numerical strings remain unchanged.

## Build from the readable source tree

With CPython 3.10+, a local LaTeX engine and BibTeX, run from the repository root:

```sh
python -B paper/tools/build_paper.py --output ../i3322-paper-build/paper_v0_1_2.pdf
```

The byte-preserved helper disables shell escape and writes PDF/log outside this source tree. Its historical default filename is superseded by the explicit output above. It installs nothing. Byte-identical PDFs across toolchains are not promised. Full mathematical replay requires the privately retained sealed reviewer asset, as described in [REPRODUCE.md](../REPRODUCE.md).

The v0.1.1 package/PDF hashes are retained as historical build-QA provenance in [PROJECT_HISTORY.md](../docs/PROJECT_HISTORY.md). The historical ZIP is privacy-withheld; the old PDF may be retained privately. Those hashes are not the current public paper identity. Historical build notes inside old seals are not current build status. Owner-authored manuscript/prose is CC BY 4.0; embedded third-party and pre-existing frozen artifacts retain their existing notices/rights under the [license map](../LICENSE).
