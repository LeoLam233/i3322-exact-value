"""Hash-check the release assets, then run the unchanged sealed paper replay wrapper."""
import argparse
import os
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from verify_hashes import require
from verify_release_assets import safe_extract, verify_assets

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--assets-dir', type=Path, required=True)
    parser.add_argument('--work-dir', type=Path, required=True, help='Fresh directory outside repository and assets')
    parser.add_argument('--full', action='store_true')
    args = parser.parse_args()
    require(__debug__, 'Run without Python optimization')
    assets, work = args.assets_dir.resolve(), args.work_dir.resolve()
    require(not work.is_relative_to(ROOT) and not work.is_relative_to(assets),
            'Work directory must be outside repository and assets')
    require(not work.exists(), 'Work directory must be fresh')
    verify_assets(assets, private_review=True)
    work.mkdir(parents=True)
    paper = safe_extract(assets / 'I3322_PAPER_V0_1_2.zip', work / 'paper')
    command = [sys.executable, '-B', 'tools/replay_frozen.py', '--work-dir', str(work / 'replay')]
    if args.full:
        command.append('--full')
    env = dict(os.environ)
    env.pop('PYTHONOPTIMIZE', None)
    env['PYTHONIOENCODING'] = 'utf-8'
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    result = subprocess.run(command, cwd=paper, env=env)
    require(result.returncode == 0, 'Frozen replay failed; inspect retained work logs')
    print('CANONICAL FROZEN REPLAY: PASS')

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('CANONICAL FROZEN REPLAY: FAIL: ' + str(exc), file=sys.stderr)
        raise SystemExit(1)
