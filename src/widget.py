def mask_card_number(card_number: str): -> str:
    """Маскируем номер карты, оставляя первые 4 и последние 4 цифры"""
    return card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]


def mask_account_number(account_number: str) -> str:
   """Маскируем номер счета, оставляя последние 4 цифры"""
       return '**' + account_number[-4:]


def mask_account_card(info: str) -> str:
    """Разделяем тип и номер"""
    parts = info.split()
    card_type = ' '.join(parts[:-1])  # Все кроме последнего элемента
    number = parts[-1]  # Последний элемент - номер
    if 'Счет' in card_type:
        masked_number = mask_account_number(number)
    else:
        masked_number = mask_card_number(number)

    return f"{card_type} {masked_number}"


def get_date(date: str) -> str:
    """ Разделяем строку на дату и время"""
    date_part = date_str.split('T')[0]
    year, month, day = date_part.split('-')
    return f"{day}.{month}.{year}" #Форматируем дату в нужный формат
