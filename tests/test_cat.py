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
