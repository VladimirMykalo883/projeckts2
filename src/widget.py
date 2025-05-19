from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_type: str) -> str:
    """Функция принимает тип и номер карты или счета и возвращает строку с замаскированным номером"""
    length_name_card_or_account = 0
    # В цикле определяем длину части строки не являющуюся номером счета
    for char in number_type:
        if not char.isdigit():
            length_name_card_or_account += 1
    # определяем счет или карта
    if "Счет" in number_type or "счет" in number_type:
        number_mask = get_mask_account(number_type[length_name_card_or_account:])
        return "".join(number_type[0:length_name_card_or_account] + number_mask)
    else:
        number_mask = get_mask_card_number(number_type[length_name_card_or_account:])
        return "".join(number_type[0:length_name_card_or_account] + number_mask)


def get_date(user_date: str) -> str:
    """Функция преобразует входную дату и время в короткий вариант"""
    if len(user_date) < 19:  # Проверка на длину строки, чтобы избежать IndexError
        raise IndexError("Некорректный формат даты")

    return f"{user_date[8:10]}.{user_date[5:7]}.{user_date[0:4]}"


number_type = 'Счет12346700901278564356'  # введите номер счета или карты
print(mask_account_card(number_type))

user_date = "2018-06-30T02:08:58.425572"  # "Введите дату"
print(get_date(user_date))
