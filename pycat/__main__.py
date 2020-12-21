"""
Here be awesome code!
"""
import click

from pycat.cats import Cat


@click.command()
@click.option("--strategy", default="simple", help="cat-ing strategy")
@click.option("--keep_history", default=True, type=bool)
@click.argument("filenames")
def main(filenames, strategy="simple", keep_history=True):
    cat = Cat(strategy=strategy, keep_history=keep_history)

    cat(filenames)


if __name__ == "__main__":
    main(None)
