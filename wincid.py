import json
import random
from argparse import ArgumentParser
from uuid import uuid4


def main(args):
    iddb = get_iddb()

    new_id = uuid4().hex

    if not args.no_save:
        iddb[new_id] = {'human_name': args.human_name}
        update_iddb(iddb)

    # Pipe-friendly print
    print(new_id, end='')


def update_iddb(iddb):
    # TODO: Put this somewhere central.
    json.dump(iddb, open('iddb.json', 'w'))


def get_iddb():
    # TODO: Get this from somewhere central.
    iddb = json.load(open('iddb.json'))
    return iddb


if __name__ == '__main__':
    ap = ArgumentParser('Generate Winc IDs')
    ap.add_argument('human_name', help='Human-friendly name for this UUID.\
                                        Does not need to be unique.')
    ap.add_argument('-n', '--no-save', action='store_true',
                    help='Skip saving to db.')
    args = ap.parse_args()
    main(args)
