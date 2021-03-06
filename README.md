# PyCat

PyCat is a toy implementation of `cat` in python. It has a basic
file-history feature and two 'cating' strategies.

## Usage

0. Install [poetry](https://python-poetry.org/)
1. Clone
2. `poetry install`
3. `poetry run python pycat <file_to_cat>`

## Optional Arguments

* `strategy` — `simple` or `sys_write`. See `cats.py` for implementation details
* `keep_history` — boolean, defaults to True. Controls history

## History

History is kept at `.pycat_history.json` inside the
user's folder. It is limited to 10 entries.

You can open the most recent file with `pycat #0`. In some
shells such as `zsh` you need to escape with single quotes,
`pycat '#0'`.

Accessing the rest of the history is made relatively to the most recently
opened file. `#0` being the most recent, `#1` the second most recent
and so on.
