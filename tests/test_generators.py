import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 12345678901234567890",
            "to": "Счет 09876543210987654321",
        },
        {
            "id": 142264269,
            "state": "CANCELLED",
            "date": "2020-01-01T00:00:00.000000",
            "operationAmount": {"amount": "1000.00", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Отмена перевода",
            "from": "Счет 12345678901234567891",
            "to": "Счет 09876543210987654320",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    ]


# @pytest.mark.usefixtures("transactions")


def test_generate_transactions(sample_transactions):
    # Присваиваем результат функции
    result = list(filter_by_currency(sample_transactions, "USD"))

    # Проверяем количество транзакций с состоянием "USD"
    assert len(result) == 3

    # Проверяем правильность данных первых двух транзакций
    assert result[0]["id"] == 939719570
    assert result[0]["operationAmount"]["amount"] == "9824.07"
    assert result[1]["id"] == 142264268
    assert result[1]["operationAmount"]["amount"] == "79114.93"


def test_empty_transactions():
    # Проверяем результат при передаче пустого списка
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions(sample_transactions):
    generator = transaction_descriptions(sample_transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Отмена перевода"
    assert next(generator) == ""


# def test_card_number_generator_invalid_range():
# Тестируем неправильный диапазон
#   with pytest.raises(ValueError, match="Диапазон должен быть от"):
#       list(card_number_generator(-1, 5))  # Отрицательное число

#    with pytest.raises(ValueError, match="Диапазон должен быть от"):
#        list(card_number_generator(0, 10000000000000000))  # Слишком большое число


def test_card_number_generator_invalid_order():
    # Тестируем неправильный порядок (start > end)
    with pytest.raises(ValueError, match="Начальное значение должно быть меньше"):
        list(card_number_generator(10, 5))


def test_card_number_generator_edge_cases():
    # Проверяем граничные случаи
    first = next(card_number_generator(0, 0))
    assert first == "0000 0000 0000 0000"

    last = next(card_number_generator(9999999999999999, 9999999999999999))
    assert last == "9999 9999 9999 9999"
