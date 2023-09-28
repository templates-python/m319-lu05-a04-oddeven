from o import main


def test_even(capsys, monkeypatch):
    inputs = iter([18])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Number 18 is even\n'

def test_odd(capsys, monkeypatch):
    inputs = iter([37])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Number 37 is odd\n'
