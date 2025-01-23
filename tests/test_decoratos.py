import pytest


def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def test_log_success(capsys):
    result = add(2, 3)
    captured = capsys.readouterr()
    assert result == 5


def test_log_divide_success(capsys):
    result = divide(10, 2)
    captured = capsys.readouterr()
    assert result == 5


def test_log_divide_zero_error(capsys):
    with pytest.raises(Exception):
        divide(10, 0)
    captured = capsys.readouterr()
    assert captured.out == ""
