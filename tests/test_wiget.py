import pytest
# import datetime
from src.widget import get_date, mask_account_card


# Определяем фикстуру
@pytest.fixture
def card_number():
    return "visa classic 1234567890123456"


# Передаем фикстуру в тестовую функцию
def test_mask_account_card(card_number):
    masked_number = mask_account_card(card_number)
    assert masked_number == "visa classic 1234 56** **** 3456"


# Определяем фикстуру2
@pytest.fixture
def card_number2():
    return "Счет 12345678908097123456"


# Передаем фикстуру2 в тестовую функцию
def test_mask_account_card2(card_number2):
    masked_number2 = mask_account_card(card_number2)
    assert masked_number2 == "Счет **3456"


class Test_Get_Date:

    def test_valid_date(self):
        assert get_date("2023-10-15T14:30:00") == "15.10.2023"
        assert get_date("2020-01-01T00:00:00") == "01.01.2020"
        assert get_date("1999-12-31T23:59:59") == "31.12.1999"

    def test_incorrect_format(self):
        with pytest.raises(IndexError):
            get_date("2023/10/15")  # Неверный формат даты
        with pytest.raises(IndexError):
            get_date("15-10-2023")  # Неверный формат даты

    def test_empty_string(self):
        with pytest.raises(IndexError):
            get_date("")  # Пустая строка
