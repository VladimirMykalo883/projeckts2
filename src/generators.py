from typing import List, Dict, Any, Iterator, Generator


def filter_by_currency(transactions_list: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Фильтрует транзакции по заданной валюте и возвращает итератор."""

    for transaction in transactions_list:

        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Генератор, который возвращает описание каждой транзакции по очереди."""
    for transaction in transactions:
        # Проверяем наличие ключа "description" и возвращаем его значение, если оно существует
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, Any, None]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    if start > end:
        raise ValueError("Начальное значение должно быть меньше конечного значения")
    for number in range(start, end + 1):
        # Форматируем номер карты с ведущими нулями для достижения длины 16 символов
        formatted_number = f"{number:016}"  # Форматируем номер в 16-значный
        # Разделяем на группы по 4 цифры для вывода
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:]}"
