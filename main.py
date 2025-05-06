import src.masks

account_number = input("Введите номер счета\n")
# Печатаем маску счета
print(src.masks.get_mask_account(account_number))
# Печатаем маску карты
masked_card_result_with_masks = input("Введите номер карты\n")
print(src.masks.get_mask_card_number(masked_card_result_with_masks))
