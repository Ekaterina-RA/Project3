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
