# wincid

Manages Winc IDs for you. When you create an assignment:

```bash
$ python wincid.py example
eb774aff735d4bdd9fdf71d8b3e39fef
```

WincID uses `git` on your shell to sync `iddb.json` to the remote on GitHub, so
you need `git` in your `$PATH` and preferably an internet connection. If the
pull/push fails you need to do it later manually. The same goes for merge
conflicts, although they are unlikely to occur in normal use.

To deprecate an existing item, add the `--update`-option with the Winc ID of
the item to deprecate.

* To read `iddb.json`, use `grep` or `jq`.
* If you must manually edit `iddb.json`, don't forget to increment the value
  for `revision`.

## Usage

```
usage: Generate and save Winc IDs [-h] [-d] [-u WINC_ID] human_name

positional arguments:
  human_name            Human-friendly name to pair with the new Winc ID. Does
                        not need to be unique.

optional arguments:
  -h, --help            show this help message and exit
  -d, --dry-run         Skip saving to db.
  -u WINC_ID, --update WINC_ID
                        Winc ID of assignment to mark deprecated and point to
                        the new item.
```

Tip: pipe the output Winc ID directly to your clipboard, there's no newline.

## FAQ

* What's a Winc ID?

Winc IDs are 32-character hexadecimal string representations of UUIDs. This
tool generates one by way of [Python's uuid4 function](https://docs.python.org/3/library/uuid.html#uuid.uuid4)
and saves it in `iddb.json` together with a non-unique `human_name` of choice.

## TODO

- [x] Create a central place where `iddb.json` lives, that wincid interacts
      with.
- [x] Create update mechanism.
- [ ] Turn `wincid` into a proper CLI (`pip`-installable, in `$PATH`, etc.)
- [ ] Integrate with [wincpy](https://github.com/WincAcademy/wincpy).
