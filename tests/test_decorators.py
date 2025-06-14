import pytest

from src.decorators import log
'''Тесты декоратора'''

@log()
def add(a, b): # функция  сложения
    return a + b


@log()
def raise_value_error(x): # Ошибка
    raise ValueError("Ошибка!")


@log()
def no_params(): #  Нет параметров
    return "Нет параметров"


@log("test_log.txt")
def add_file(a, b):
    return a + b


@log("test_log.txt")
def raise_key_error(x):
    raise KeyError("Ключ не найден")


def test_success_console(capsys):
    result = add(2, 3)
    captured = capsys.readouterr()
    assert result == 5
    assert "Функция 'add' успешно выполнена" in captured.out
    assert "Результат: 5" in captured.out


def test_exception_console(capsys):
    with pytest.raises(ValueError):
        raise_value_error(42)
        captured = capsys.readouterr()
        assert "Функция 'raise_value_error' вызвала ошибку 'ValueError'" in captured.out
        assert "Параметры: 42" in captured.out


def test_no_params_console(capsys):
    result = no_params()
    captured = capsys.readouterr()
    assert result == "Нет параметров"
    assert "Функция 'no_params' успешно выполнена" in captured.out


def test_success_file(tmp_path):
    log_path = tmp_path / "log.txt"

    @log(str(log_path))
    def multiply(a, b):
        return a * b
    res = multiply(3, 4)
    assert res == 12
    content = log_path.read_text(encoding="utf-8")
    assert "Функция 'multiply' успешно выполнена" in content
    assert "Результат: 12" in content


def test_exception_file(tmp_path):
    log_path = tmp_path / "log.txt"

    @log(str(log_path))
    def fail(x):
        raise RuntimeError("Ошибка выполнения")
    with pytest.raises(RuntimeError):
        fail("тест")
    content = log_path.read_text(encoding="utf-8")
    assert "Функция 'fail' вызвала ошибку 'RuntimeError'" in content
    assert "Параметры: 'тест'" in content
