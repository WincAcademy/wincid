import json
from random import randint


def main():
    iddb = get_iddb()
    new_id = gen_new_id(iddb)
    update_iddb(iddb, new_id)
    print(new_id)


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
    a = adjectives[randint(0, 99)]
    n = nouns[randint(0, 99)]
    return f'{a}-{n}-{randint(0, 99)}'


def get_iddb():
    iddb = json.load(open('iddb.json'))
    return iddb


def update_iddb(iddb, new_id):
    iddb[new_id] = {}
    json.dump(iddb, open('iddb.json', 'w'))


if __name__ == '__main__':
    main()
