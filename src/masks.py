def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    masked_number = ""
    for i in range(len(card_number)):
        if i < 6 or i >= len(card_number) - 4:
            masked_number += card_number[i]
        elif card_number[i].isdigit():
            masked_number += "*"
        else:
            masked_number += ""
    masked_number = " ".join(
        [masked_number[i: i + 4] for i in range(0, len(masked_number), 4)]
    )

    return masked_number


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if len(account_number) < 4:
        return account_number
    masked_account = "**" + account_number[-4:]
    return masked_account
