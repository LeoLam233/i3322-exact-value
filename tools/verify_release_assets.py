"""Verify release assets against repository pins, and optionally the full audit bundle."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile
sys.dont_write_bytecode = True
from verify_hashes import parse_manifest, require, safe_name, sha256, verify_tree

ROOT = Path(__file__).resolve().parents[1]

def zip_inventory(archive):
    names, folded = set(), set()
    for info in archive.infolist():
        safe_name(info.filename)
        key = info.filename.casefold().rstrip('/')
        require(key not in folded, 'Duplicate/case-colliding ZIP member')
        folded.add(key)
        require(not info.flag_bits & 1, 'Encrypted ZIP member')
        require((info.external_attr >> 16) & 0o170000 != 0o120000, 'ZIP symlink')
        if not info.is_dir():
            names.add(info.filename)
    require(archive.testzip() is None, 'ZIP CRC failure')
    return names

def verify_bundle(path):
    prefix = 'I3322_FULL_AUDIT_BUNDLE_v0.1/'
    with zipfile.ZipFile(path) as archive:
        names = zip_inventory(archive)
        manifest_name = prefix + 'MANIFEST.sha256'
        entries = parse_manifest(archive.read(manifest_name).decode('utf-8'))
        require(names == {prefix + n for n in entries} | {manifest_name}, 'Bundle inventory mismatch')
        for name, expected in entries.items():
            require(hashlib.sha256(archive.read(prefix + name)).hexdigest() == expected,
                    'Bundle member hash mismatch: ' + name)
        pins = json.loads((ROOT / 'provenance/artifact_index.json').read_text(encoding='utf-8'))
        for item in pins['principal_artifacts'] + pins.get('historical_paper_artifacts', []):
            require(entries.get('assets/' + item['filename']) == item['sha256'], 'Bundle authority pin mismatch')
    return len(entries)

def verify_assets(directory, check_bundle=False, private_review=False):
    directory = Path(directory).resolve()
    supplied = directory / 'SHA256SUMS'
    expected = ROOT / ('release/PRIVATE_REVIEW_SHA256SUMS' if private_review else 'release/SHA256SUMS')
    require(supplied.read_bytes() == expected.read_bytes(), 'Release manifest differs from repository pin')
    entries = verify_tree(directory, 'SHA256SUMS')
    pins = json.loads((ROOT / 'provenance/artifact_index.json').read_text(encoding='utf-8'))
    if private_review:
        for item in pins['principal_artifacts'] + pins.get('historical_paper_artifacts', []):
            require(entries.get(item['filename']) == item['sha256'], 'Private reviewer asset hash mismatch')
        if check_bundle:
            verify_bundle(directory / 'I3322_FULL_AUDIT_BUNDLE_v0.1.zip')
    else:
        withheld = {x['filename'] for x in pins['public_release_policy']['withheld_for_personal_metadata']}
        require(not (withheld & set(entries)), 'Privacy-withheld artifact present in public release assets')
        for item in pins.get('public_release_assets', []):
            require(entries.get(item['filename']) == item['sha256'], 'Public release asset hash mismatch: ' + item['filename'])
        require(not check_bundle, 'Full audit bundle is private-review only')
    return entries

def safe_extract(source, destination):
    destination = Path(destination)
    require(not destination.exists(), 'Extraction destination must be fresh')
    with zipfile.ZipFile(source) as archive:
        zip_inventory(archive)
        destination.mkdir(parents=True)
        archive.extractall(destination)
    roots = list(destination.iterdir())
    require(len(roots) == 1 and roots[0].is_dir(), 'Expected a single archive root')
    return roots[0]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--assets-dir', type=Path, required=True)
    parser.add_argument('--bundle', action='store_true')
    parser.add_argument('--private-review', action='store_true', help='Verify the original full reviewer asset tree instead of the privacy-filtered public Release')
    args = parser.parse_args()
    entries = verify_assets(args.assets_dir, args.bundle, args.private_review)
    profile = 'private-review' if args.private_review else 'public'
    print(f'RELEASE ASSETS: PASS ({len(entries)} files; profile={profile}; bundle checked={args.bundle})')

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('RELEASE ASSETS: FAIL: ' + str(exc), file=sys.stderr)
        raise SystemExit(1)
