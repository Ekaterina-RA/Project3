from src import masks, widget


print(masks.get_mask_card_number(7000792289606361))
print(masks.get_mask_account(73654108430135874305))

print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))

print(get_date("2024-03-11T02:26:18.671407"))
print(get_date("2023-12-25T15:30:00.000000"))