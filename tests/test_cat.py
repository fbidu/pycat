from pycat import cat, Cat


def test_cat_works(capsys):
    cat("tests/hello.txt", "tests/world.txt")
    captured = capsys.readouterr()
    assert captured.out == "hello, world!"


def test_cat_strategy(capsys):
    cat = Cat(strategy="simple")
    cat("tests/hello.txt")
    captured = capsys.readouterr()
    assert captured.out == "hello"


def test_cat_sys_write(capsys):
    cat = Cat(strategy="sys_write")
    cat("tests/hello.txt")
    captured = capsys.readouterr()
    assert captured.out == "hello"


def test_cat_accepts_dry_run(capsys):
    """
    Sometimes we don't want to
    actually print anything
    """
    cat("tests/hello.txt", dryrun=True)
    captured = capsys.readouterr()
    assert captured.out == ""


def test_cat_keeps_history(capsys):
    """
    We want to be able to open a previously opened
    file by its index:

    >> cat('file1')
    <file 1 content>
    >> cat('file2')
    <file 2 content>

    >> cat('$0')
    <file 2 content>
    >> cat('$1')
    <file 1 content
    """
    cat("tests/hello.txt")
    cat("$0")
    captured = capsys.readouterr()
    assert captured.out == "hello"
