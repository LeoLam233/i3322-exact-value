"""Check repository links, frozen-source pins, exact theorem strings and scope/status invariants."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

sys.dont_write_bytecode = True
from verify_hashes import require, sha256

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {'.md', '.tex', '.bib', '.py', '.json', '.template', '.sha256', '.txt', '.cff', '.yml', '.yaml'}

def anchor_ids(text):
    slugs, counts = set(), {}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, flags=re.M):
        plain = re.sub(r'[`*_]', '', heading).lower()
        plain = re.sub(r'[^\w\-\s]', '', plain).replace(' ', '-')
        count = counts.get(plain, 0)
        counts[plain] = count + 1
        slugs.add(plain if count == 0 else f'{plain}-{count}')
    return slugs

def check(root):
    root = root.resolve()
    required = ['README.md', 'THEOREM.md', 'AUDIT_ME_FIRST.md', 'REPRODUCE.md',
        'PROVENANCE.md', 'LIMITATIONS.md', 'AUTHORSHIP.md', 'LICENSE', 'LICENSES/MIT.txt', 'LICENSES/CC-BY-4.0.txt', 'THIRD_PARTY_NOTICES.md', 'PUBLICATION_CHECKLIST.md',
        'CITATION.cff', '.gitignore', 'paper/main.tex', 'paper/references.bib',
        'paper/paper_v0_1_2.pdf', 'proof/DEPENDENCY_GRAPH.md', 'proof/THEOREM_CROSSWALK.md',
        'proof/EXTERNAL_PREMISES.md', 'proof/MACHINE_ANALYTIC_BOUNDARY.md', 'machine/README.md',
        'audit/README.md', 'audit/FINAL_INTEGRATED_AUDIT.md', 'audit/SOURCE_PROVENANCE_AUDIT.md',
        'provenance/ARTIFACT_HASHES.md', 'provenance/SOURCE_RELIABILITY.md',
        'provenance/KNOWN_SOURCE_ISSUES.md', 'rejected/README.md', 'rejected/SOL_O6_ARITHMETIC_FAILURE.md',
        'docs/PROJECT_HISTORY.md', 'docs/VALIDATION_STATUS.md', 'docs/REPOSITORY_ARCHITECTURE.md', 'docs/PUBLICATION_PATCH_CHECKS.json',
        'tools/verify_hashes.py', 'tools/verify_release_assets.py',
        'release/RELEASE_NOTES_v0.1.0.md', 'release/RELEASE_NOTES_v0.1.1.md',
        'release/RELEASE_ASSETS.md', 'release/SEALED_ARTIFACT_PRIVACY.md',
        'release/PRIVATE_REVIEW_SHA256SUMS', 'release/SHA256SUMS', 'release/SHA256SUMS_v0.1.1']
    for name in required:
        require((root / name).is_file(), 'Required file missing: ' + name)
    require((root / 'LICENSE').is_file() and (root / 'CITATION.cff').is_file(),
            'Final public metadata missing')
    pins = json.loads((root / 'provenance/artifact_index.json').read_text(encoding='utf-8'))
    preservation = json.loads((root / 'provenance/source_preservation.json').read_text(encoding='utf-8'))
    for item in preservation['files']:
        require(sha256(root / item['repository_path']) == item.get('current_sha256', item['sha256']),
                'Pinned public source/PDF changed: ' + item['repository_path'])
    lower, upper = pins['root_certificate']['s_enclosure']
    for name in ['README.md', 'THEOREM.md', 'docs/PROJECT_HISTORY.md']:
        text = (root / name).read_text(encoding='utf-8')
        require(lower in text and upper in text, 'Missing or changed endpoint string: ' + name)
    require(Fraction(upper) - Fraction(lower) == Fraction(pins['root_certificate']['exact_width']),
            'Exact width does not agree with endpoints')
    require(Fraction('0.2508753845139765') < Fraction(lower) < Fraction(upper) < Fraction('0.2508753855'),
            'Root bracket escaped clean domain')
    for name in ['README.md', 'LIMITATIONS.md', 'docs/VALIDATION_STATUS.md']:
        text = (root / name).read_text(encoding='utf-8')
        for token in ['OPEN-MINOR', 'CLOSED-PASS', 'M001']:
            require(token in text, 'Missing preserved status: ' + name)

    canonical_url = 'https://github.com/LeoLam233/i3322-exact-value'
    require(canonical_url in (root / 'README.md').read_text(encoding='utf-8'), 'Canonical repository URL missing from README')
    require(canonical_url in (root / 'CITATION.cff').read_text(encoding='utf-8'), 'Canonical repository URL missing from CITATION.cff')
    for path in root.rglob('*'):
        if path.is_file() and path.suffix in TEXT_SUFFIXES:
            txt = path.read_text(encoding='utf-8')
            private_domain = '@' + 'gmail.com'
            require(private_domain not in txt.lower(), 'Private Gmail-domain address leaked in readable repository: ' + path.relative_to(root).as_posix())

    limits = (root / 'LIMITATIONS.md').read_text(encoding='utf-8')
    for token in ['finite-dimensional/projective tensor', 'No R2', 'No finite-dimensional attainment',
                  'No optimizer uniqueness', 'No elementary closed-form', 'unresolved', 'pending', 'unpatched']:
        require(token in limits, 'Missing limitation: ' + token)
    for name in ['rejected/README.md', 'rejected/SOL_O6_ARITHMETIC_FAILURE.md']:
        require('REJECTED — NOT THEOREM AUTHORITY' in (root / name).read_text(encoding='utf-8'),
                'Rejected status missing')
    forbidden = re.compile(r'(?:[A-Z]:[/\\]Users[/\\]|/(?:mnt)/[a-z]/(?:Users)/|/(?:mnt)/(?:data)/|/(?:home|Users)/[^/\s]+/|sand(?:box):)', re.I)
    forbidden_files = {'.pyc', '.pyo', '.aux', '.bbl', '.blg', '.fls', '.fdb_latexmk', '.log', '.zip'}
    links, tex_inputs, text_files = 0, 0, 0
    for path in root.rglob('*'):
        relative = path.relative_to(root)
        if relative.parts[0] == '.git':
            continue
        require(not path.is_symlink(), 'Unexpected symlink')
        require('__pycache__' not in relative.parts, 'Interpreter cache in repository')
        if not path.is_file():
            continue
        require(path.suffix not in forbidden_files, 'Unexpected build/binary archive file: ' + relative.as_posix())
        if path.suffix not in TEXT_SUFFIXES and path.name not in {'.gitignore', 'SHA256SUMS', 'LICENSE'}:
            continue
        text = path.read_text(encoding='utf-8')
        text_files += 1
        require(not forbidden.search(text), 'Local path marker in: ' + relative.as_posix())
        if path.suffix == '.md':
            for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', text):
                target = target.strip('<>')
                parsed = urlsplit(target)
                if parsed.scheme:
                    continue
                require(not target.startswith('/'), 'Absolute Markdown link')
                resolved = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
                require(resolved.is_relative_to(root), 'Link escapes repository')
                require(resolved.exists(), 'Broken link: ' + relative.as_posix() + ' -> ' + target)
                if parsed.fragment and resolved.suffix == '.md':
                    require(unquote(parsed.fragment) in anchor_ids(resolved.read_text(encoding='utf-8')),
                            'Broken heading anchor: ' + target)
                links += 1
        if path.suffix == '.tex':
            for name in re.findall(r'\\(?:input|include)\{([^}]+)\}', text):
                target = root / 'paper' / (name if name.endswith('.tex') else name + '.tex')
                require(target.is_file(), 'Missing TeX include: ' + name)
                tex_inputs += 1
    return {'status': 'PASS', 'required_files': len(required), 'local_links': links,
            'tex_includes': tex_inputs, 'text_files_scanned': text_files,
            'frozen_files_verified': len(preservation['files']), 'local_path_markers': 0,
            'exact_endpoint_strings': 'PASS', 'scope_status_invariants': 'PASS',
            'boundary': 'Static consistency checks; semantic proof/authority review is separate'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    print(json.dumps(check(args.root), indent=2))

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('REPOSITORY CHECK: FAIL: ' + str(exc), file=sys.stderr)
        raise SystemExit(1)
