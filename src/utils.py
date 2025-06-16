from dotenv import  load_dotenv, dotenv_values
import json
import os
import requests
from typing import Any, Dict, List
# Определим полный путь к файлу .env
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
json_path = os.path.join(project_root,'data','operations.json')
# print(json_path,'путь к файлу операций')
# print(os.path.exists(json_path))
"""
    Считывает список транзакций из JSON-файла.
    Args:
        json_path (str): Путь к JSON-файлу.
    Returns:
        list: Список словарей с транзакциями, либо None в случае ошибки.
    """

def read_json_files(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            # производится считывание из json файла
            list_dict_transactions = json.load(f)
        return list_dict_transactions
    except FileNotFoundError:
        print(f"Файл {json_path} не найден.")
    except json.JSONDecodeError:
        print(f"Файл {json_path} содержит некорректный JSON.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    return None


if __name__ == '__main__':
    list_dict_transactions = read_json_files(json_path)
    if list_dict_transactions is not None:
        print(f"Прочитано {len(list_dict_transactions)} транзакций.")
        print(list_dict_transactions[0])  # пример вывода первой транзакции

def convert_transaction_to_rub(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    Ожидаемый формат транзакции:
    {
        "amount": float,
        "currency": "RUB" | "USD" | "EUR" | ...
    }
    """
    amount = float(transaction.get("amount", 0))
    currency = transaction.get("currency", "RUB").upper()

    if currency == "RUB":
        return amount

    if currency in ("USD", "EUR"):
        # Получаем курс валюты к рублю
        url = f"https://api.exchangerate.host/latest?base={currency}&symbols=RUB"
        response = requests.get(url)
        response.raise_for_status()  # Проверит, что запрос успешен
        data = response.json()
        rate = data["rates"]["RUB"]
        return amount * rate

    # Если неизвестная валюта — можно либо вернуть 0, либо сумму без изменений,
    # либо выбросить ошибку. Здесь возвращаем исходную сумму.
    return amount

# Пример использования:
transaction_usd = {"amount": 10, "currency": "USD"}
print(convert_transaction_to_rub(transaction_usd))  # конвертированная сумма в рублях
