import json
from argparse import ArgumentParser
import random


def main(args):
    iddb = get_iddb()

    new_id = gen_new_id(iddb)
    if args.interactive:
        while input(f'Use \"{new_id}\"? [y/n]\n') != 'y':
            new_id = gen_new_id(iddb)

    if not args.no_save:
        update_iddb(iddb, new_id)
    print(new_id, end='')


def gen_new_id(iddb):
    adjectives = open('adjectives.txt').read().split('\n')
    nouns = open('nouns.txt').read().split('\n')

    good_id = False
    while not good_id:
        new_id = gen_id(adjectives, nouns)
        if new_id not in iddb:
            good_id = True

    return new_id


def gen_id(adjectives, nouns):
    a = random.choice(adjectives)
    n = random.choice(nouns)
    return f'{a}_{n}_{random.randint(0, 99)}'


def get_iddb():
    iddb = json.load(open('iddb.json'))
    return iddb


def update_iddb(iddb, new_id):
    iddb[new_id] = {}
    json.dump(iddb, open('iddb.json', 'w'))


if __name__ == '__main__':
    ap = ArgumentParser('Generate Winc IDs')
    ap.add_argument('-i', '--interactive', action='store_true',
                    help='Interactive mode')
    ap.add_argument('-n', '--no-save', action='store_true',
                    help='Skip saving to db.')
    args = ap.parse_args()
    main(args)
