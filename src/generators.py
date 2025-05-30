from typing import List, Dict, Any, Iterator

transactions = [
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
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions_list: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Фильтрует транзакции по заданной валюте и возвращает итератор."""
    # Проверка типа входных данных
    if not isinstance(transactions_list, list):
        raise ValueError("Ожидается список транзакций.")

    if not isinstance(currency, str):
        raise ValueError("Ожидается строка для валюты.")

    for transaction in transactions_list:

        # Проверяем, что каждая транзакция является словарем
        if not isinstance(transaction, dict):
            raise ValueError("Каждая транзакция должна быть словарем.")
        # Проверяем, содержит ли транзакция ключ 'currency'
        if "currency" not in transaction["operationAmount"]:
            raise ValueError("Каждая транзакция должна содержать ключ 'currency'.")
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Генератор, который возвращает описание каждой транзакции по очереди."""
    for transaction in transactions:
        # Проверяем наличие ключа "description" и возвращаем его значение, если оно существует
        if "description" in transaction:
            yield transaction["description"]
        else:
            yield "Описание отсутствует"  # Сообщение о том, что описания нет


def card_number_generator(start: int, end: int) -> str:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    if start > end:
        raise ValueError("Начальное значение должно быть меньше конечного значения")
    for number in range(start, end + 1):
        # Форматируем номер карты с ведущими нулями для достижения длины 16 символов
        formatted_number = f"{number:016}"  # Форматируем номер в 16-значный
        # Разделяем на группы по 4 цифры для вывода
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:]}"


# печать итераций по коду валют
code_transactions = filter_by_currency(transactions, "USD")


for transaction in code_transactions:
    print(transaction)


# Использование генератора и печать описаний
for description in transaction_descriptions(transactions):
    print(description)

# Пример использования генератора
start_number = 1
end_number = 10  # Установите нужный диапазон
for card_number in card_number_generator(start_number, end_number):
    print(card_number)
