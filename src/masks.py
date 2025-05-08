def get_mask_account(card_account: str) -> str:
    """Функция получает номер счета и выводит 2"*" и 4 последние цифры"""

    card_account = card_account.replace(" ", "")
    if len(card_account) != 20 or not card_account.isdigit():
        return "неверное количество или значение цифр"

    last_part = str(card_account[-4:])
    return f"**{last_part}"


def get_mask_card_number(card_number: str) -> str:
    """Функция вводит номер карты, проверяет и выводит маску карты"""
    card_number = card_number.replace(" ", "")
    # проверяем хватает цифр в номере карты

    if len(card_number) != 16 or not card_number.isdigit():
        # проверяем правильно ли набран номер карты и все ли символы цифры
        return "Введен неверный номер карты"
    result = []  # список для хранения замаскированного номера карты
    counter = 0  # счетчик цифр в номере карты, чтобы знать, где вводить "*"

    for number in card_number:
        counter += 1
        if 6 < counter <= len(card_number) - 4:
            result.append("*")
        else:
            result.append(number)
    masked_card = "".join(result)

    masked_card_result = []  # список для хранения по четыре цифры номера карты

    for i in range(0, len(masked_card), 4):
        masked_card_result.append(masked_card[i : i + 4])

    masked_card_result_with_space = " ".join(masked_card_result)
    return masked_card_result_with_space
