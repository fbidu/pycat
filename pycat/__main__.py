"""
Here be awesome code!
"""
import click

from pycat.cats import Cat


@click.command()
@click.option("--strategy", default="simple", help="cat-ing strategy")
@click.argument("filenames")
def main(filenames, strategy="simple"):
    cat = Cat(strategy=strategy)

    cat(filenames)


if __name__ == "__main__":
    main(None)
