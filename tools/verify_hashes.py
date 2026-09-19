"""Verify an exact SHA-256 tree inventory. Python 3.10+, standard library only."""
import argparse
import hashlib
from pathlib import Path, PurePosixPath
import re
import sys

def require(condition, message):
    if not condition:
        raise ValueError(message)

def sha256(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def safe_name(name):
    p = PurePosixPath(name)
    require(bool(name) and not p.is_absolute() and '..' not in p.parts
            and '\\' not in name and ':' not in name, 'Unsafe relative path')
    require(p.as_posix() == name.rstrip('/'), 'Noncanonical relative path')
    return p

def parse_manifest(text):
    entries, folded = {}, set()
    for line in text.splitlines():
        if not line.strip():
            continue
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        require(m is not None, 'Malformed SHA-256 manifest row')
        digest, name = m.groups()
        safe_name(name)
        require(name.casefold() not in folded, 'Duplicate/case-colliding manifest name')
        folded.add(name.casefold())
        entries[name] = digest
    require(bool(entries), 'Empty manifest')
    return entries

def verify_tree(root, manifest='MANIFEST.sha256', ignore_git=False):
    root = Path(root).resolve()
    entries = parse_manifest((root / manifest).read_text(encoding='utf-8'))
    actual, folded = set(), set()
    for p in root.rglob('*'):
        rel = p.relative_to(root)
        if ignore_git and rel.parts[0] == '.git':
            continue
        require(not p.is_symlink(), 'Symlink in sealed tree: ' + rel.as_posix())
        if p.is_file():
            name = rel.as_posix()
            require(name.casefold() not in folded, 'Case-colliding inventory')
            folded.add(name.casefold())
            actual.add(name)
    require(actual == set(entries) | {manifest}, 'Tree inventory differs from manifest')
    for name, expected in entries.items():
        require(sha256(root / name) == expected, 'SHA-256 mismatch: ' + name)
    return entries

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--manifest', default='MANIFEST.sha256')
    parser.add_argument('--ignore-git', action='store_true', help='Ignore only root .git metadata in a Git checkout')
    args = parser.parse_args()
    entries = verify_tree(args.root, args.manifest, args.ignore_git)
    print(f'TREE HASHES AND INVENTORY: PASS ({len(entries)} files)')

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('TREE VERIFICATION: FAIL: ' + str(exc), file=sys.stderr)
        raise SystemExit(1)
