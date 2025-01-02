from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date
from typing import Dict, List

print(get_mask_card_number(7000792289606361))
print(get_mask_account(73654108430135874305))

print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))

print(get_date("2024-03-11T02:26:18.671407"))
print(get_date("2023-12-25T15:30:00.000000"))



# Пример использования def filter_by_state:
list_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

# Выход функции со статусом по умолчанию 'EXECUTED'
executed_items = filter_by_state(list_dict)
print(executed_items)

# Выход функции, если вторым аргументом передано 'CANCELED'
canceled_items = filter_by_state(list_dict, key="CANCELED")
print(canceled_items)
print(canceled_items)

sorted_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
print(sorted_list)