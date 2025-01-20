import pytest


# Фикстуры для тестирования
@pytest.fixture
def card_numbers():
    return {
        "standard": "7000792289606361",
        "short": "7000",
        "edge": "786900",
        "various": "123456789012",
        "empty": "",
    }


@pytest.fixture
def account_numbers():
    return {
        "standard": "123456789012",
        "less_than_four": ["123", "12", "1"],
        "empty": "",
    }


# Фикстуры для тестирования
@pytest.fixture
def account_card_data():
    return [
        ("Карта 123456789012", "Карта 1234 56** 9012"),
        ("Счет 123456789012", "Счет **9012"),
        ("Счет 123", "Счет 123"),
        ("Карта 12", "Карта 12"),
        ("Карта 1", "Карта 1"),
        ("Счет ", " Счет"),
    ]


@pytest.fixture
def invalid_account_card_data():
    return [""]


@pytest.fixture
def date_data():
    return [
        ("2023-10-05T14:30:00", "05.10.2023"),
        ("2020-01-01T00:00:00", "01.01.2020"),
        ("2023-02-28T12:00:00", "28.02.2023"),
        ("2023-02-29T12:00:00", "29.02.2023"),
        ("2023-10-05", "05.10.2023"),
    ]


@pytest.fixture
def invalid_date_data():
    return [
        "",
        "Только буквы",
        "2023-10",
    ]


# Фикстуры для тестирования
@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4, "state": "CANCELLED"},
    ]


@pytest.fixture
def empty_data():
    return []


# Фикстуры для тестирования
@pytest.fixture
def sample_date():
    return [
        {"id": 1, "date": "2023-10-05"},
        {"id": 2, "date": "2023-09-15"},
        {"id": 3, "date": "2023-10-01"},
        {"id": 4, "date": "2023-09-20"},
    ]


@pytest.fixture
def empty_info():
    return []


@pytest.fixture
def same_date_info():
    return [
        {"id": 1, "date": "2023-10-05"},
        {"id": 2, "date": "2023-10-05"},
    ]


# Фикстура filter_by_currency
@pytest.fixture
def transactions_data():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


# Фикстура для передачи тестовых данных
@pytest.fixture
def card_number_range():
    return (1, 5)  # Пример диапазона номеров карт
