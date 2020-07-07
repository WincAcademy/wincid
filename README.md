# wincid

Manages Winc IDs for you. A little bit.

Winc IDs are 32-character hexadecimal string representations of UUIDs. This
tool generates one by way of [Python's uuid4 function](https://docs.python.org/3/library/uuid.html#uuid.uuid4)
and saves it in `iddb.json` together with a non-unique `human_name` of choice.

## Usage

```
usage: Generate Winc IDs [-h] [-d] human_name

positional arguments:
  human_name     Human-friendly name for this UUID. Does not need to be
                 unique.

optional arguments:
  -h, --help     show this help message and exit
  -d, --dry-run  Skip saving to db.
```

Tip: pipe the output directly to your clipboard, there's no newline.

## TODO

- [ ] Create a central place where `iddb.json` lives, that wincid interacts
      with.
- [ ] Turn `wincid` into a proper CLI (`pip`-installable, in `$PATH`, etc.)
- [ ] Integrate with [wincpy](https://github.com/WincAcademy/wincpy).
