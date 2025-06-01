"""import src.masks
import src.widget
import src.processing
"""

from src.processing import filter_by_state, sort_by_date
# from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


"""account_number = input("Введите номер счета\n")
     Печатаем маску счета
     print(src.masks.get_mask_account(account_number))
     Печатаем маску карты
     masked_card_result_with_masks = input("Введите номер карты\n")
     print(src.masks.get_mask_card_number(masked_card_result_with_masks))
     функции относятся к другим модулям и еще понадобятся в дальнейшем
"""
operations_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 623454892, "state": "EXECUTED", "date": "2018-11-16T08:23:53.419441"},
]
# state_key = input("Введите значение state")
state_key = "EXECUTED"
if not state_key.isalpha():
    state_key = "EXECUTED"
# переходим в модуль processing.py   с возможностью поменять ключ фильтрации

filtered = filter_by_state(operations_list, state := state_key)

sorted_operations = sort_by_date(filtered)

for operation in sorted_operations:
    print(operation)
