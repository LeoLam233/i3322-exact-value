"""Build main.tex offline in a temporary directory, preserving the source seal."""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT.parent/"paper_v0_1.pdf")
    args = parser.parse_args()
    engine = next((shutil.which(x) for x in
                   ("pdflatex", "lualatex", "xelatex") if shutil.which(x)), None)
    bibtex = shutil.which("bibtex")
    if not engine or not bibtex:
        print("PAPER LATEX BUILD: NOT AVAILABLE")
        print("Requires a local LaTeX engine and BibTeX. No downloads attempted.")
        return 2
    output = args.output.resolve()
    if output.is_relative_to(ROOT):
        raise RuntimeError("Choose a PDF output outside the sealed source directory")
    with tempfile.TemporaryDirectory(prefix="i3322-paper-build-") as name:
        work = Path(name)
        for path in ROOT.rglob("*"):
            if path.is_file() and path.suffix in {".tex", ".bib"}:
                dest = work/path.relative_to(ROOT)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, dest)
        latex = [engine, "-interaction=nonstopmode", "-halt-on-error",
                 "-no-shell-escape", "main.tex"]
        for command in (latex, [bibtex, "main"], latex, latex):
            result = subprocess.run(command, cwd=work, capture_output=True)
            if result.returncode:
                print(result.stdout.decode("utf-8", errors="replace"))
                print(result.stderr.decode("utf-8", errors="replace"))
                return result.returncode
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(work/"main.pdf", output)
        shutil.copyfile(work/"main.log", output.with_suffix(".build.log"))
    print("PAPER LATEX BUILD: PASS")
    print(output)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
