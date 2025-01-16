import pytest

from src.generators import filter_by_currency


@pytest.mark.parametrize(
    "currency, expected",
    [
        ("USD", 3),  # Ожидаем 3 транзакции в USD
        ("RUB", 2),  # Ожидаем 2 транзакции в RUB
        ("EUR", 0),  # Ожидаем 0 транзакций в EUR
    ],
)
def test_filter_by_currency(transactions_data, currency, expected):
    result = list(filter_by_currency(transactions_data, currency))
    assert len(result) == expected


def test_filter_with_empty_transaction_list():
    result = list(filter_by_currency([], "USD"))
    assert result == []  # Ожидаем пустой список


def test_filter_with_no_transactions_in_given_currency(transactions_data):
    no_currency_transactions = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01T01:00:00",
            "operationAmount": {
                "amount": "1000.00",
                "currency": {"name": "GBP", "code": "GBP"},
            },
            "description": "Перевод в GBP",
            "from": "Счет 123456789",
            "to": "Счет 987654321",
        }
    ]
    result = list(filter_by_currency(no_currency_transactions, "USD"))
    assert result == []  # Ожидаем пустой список


if __name__ == "__main__":
    pytest.main()
