import pytest

from src.widget import get_date, mask_account_card


# Тесты для функции mask_account_card
def test_mask_account_card(account_card_data):
    for input_data, expected_result in account_card_data:
        assert mask_account_card(input_data) == expected_result


def test_mask_account_card_invalid(invalid_account_card_data):
    for input_data in invalid_account_card_data:
        with pytest.raises(IndexError):
            mask_account_card(input_data)


# Тесты для функции get_date
def test_get_date(date_data):
    for input_date, expected_result in date_data:
        assert get_date(input_date) == expected_result


def test_get_date_invalid(invalid_date_data):
    for input_date in invalid_date_data:
        with pytest.raises(ValueError):
            get_date(input_date)
