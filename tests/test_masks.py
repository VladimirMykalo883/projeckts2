import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('value, expected',
                         [
                             ('12345678909087654321', '**4321'),
                             ('123456789090876543212', 'неверное количество или значение цифр'),
                             ('1234567890987654321', 'неверное количество или значение цифр'),
                             ('', 'неверное количество или значение цифр'),
                             ('12345 678901234567l89', 'неверное количество или значение цифр'),
                         ])
def test_get_masks_account(value, expected):
    assert get_mask_account(value) == expected


@pytest.mark.parametrize('value, expected',
                         [
                             ('1234567890123456', '1234 56** **** 3456'),
                             ('123456789021345', 'Введен неверный номер карты'),
                             ('12345678901234567', 'Введен неверный номер карты'),
                             ('', 'Введен неверный номер карты'),
                             ('123l456789023456', 'Введен неверный номер карты'),
                             ('12345 6789012345', 'Введен неверный номер карты'),
                         ])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected

    def test_empty_string(self):
        with pytest.raises(IndexError):
            get_mask_card_number("")  # Пустая строка