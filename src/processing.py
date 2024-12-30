def filter_by_state(data: str, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей, каждый из которых должен содержать ключ 'state'.
    :param state: Значение для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список, содержащий только те словари, у которых ключ 'state' соответствует указанному значению.
    """
    return [item for item in data if item.get('state') == state]



def sort_by_date(base_idtime, reverse=False):
    return sorted(base_idtime, key = lambda x: [x]['date'], reverse=reverse)
print(sorted)
