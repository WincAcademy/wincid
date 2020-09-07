import json
import subprocess
import sys
from argparse import ArgumentParser
from datetime import datetime as dt
from uuid import uuid4


def main(args):
    iddb_path = 'iddb.json'
    iddb = get_iddb(iddb_path)

    new_id = uuid4().hex

    if args.update:
        try:
            iddb[args.update]['superseded_by'] = new_id
        except KeyError:
            sys.stderr.write(f"Error: '{args.update}' does not exist in iddb. "
                             + 'Exiting without writing anything.\n')
            sys.exit(1)

    iddb[new_id] = {
        'human_name': args.human_name,
        'created': dt.now().isoformat(),
        'superseded_by': '',
    }
    iddb['version'] += 1

    if args.dry_run:
        print('DRY RUN')
        print(f'Would have updated {args.update}')
        print(iddb[new_id])
        sys.exit(0)

    update_iddb(iddb_path, iddb)

    print(new_id, end='')


def update_iddb(iddb_path, iddb):
    json.dump(iddb, open(iddb_path, 'w'), indent=4)
    try:
        subprocess.run(['git', 'add', iddb_path], check=True)
        subprocess.run(
            ['git', 'commit', '-m', '"Auto-update iddb"', '--quiet'],
            check=True)
        subprocess.run(['git', 'push', '--quiet'], check=True)
    except subprocess.CalledProcessError:
        sys.stderr.write('Error: git add/commit/push steps failed; '
                         + 'iddb was written but not pushed to GitHub\n')


def get_iddb(iddb_path):
    # TODO: Get this from somewhere central.
    iddb = json.load(open(iddb_path))
    try:
        subprocess.run(['git', 'pull', '-q', '--commit'], check=True)
    except subprocess.CalledProcessError:
        sys.stderr.write('Error: git pull step failed; '
                         + 'iddb was not updated before write action')
    return iddb


if __name__ == '__main__':
    ap = ArgumentParser('Generate and save Winc IDs')
    ap.add_argument('human_name',
                    help='Human-friendly name to pair with the new Winc ID. Does not need to be unique.')
    ap.add_argument('-d', '--dry-run', action='store_true',
                    help='Skip saving to db.')
    ap.add_argument('-u', '--update', type=str, required=False, default=False, metavar='WINC_ID',
                    help='Winc ID of assignment to mark deprecated and point to the new item.')
    args = ap.parse_args()
    main(args)
