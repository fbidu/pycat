from pycat import cat


def test_cat_works(capsys):
    cat("tests/hello.txt")
    captured = capsys.readouterr()
    assert captured.out == "hello, world!"
