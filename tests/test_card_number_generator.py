import pytest

from src.generators import card_number_generator


# Параметризованный тест для проверки корректных номеров карт
@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            4000000000000000,
            4000000000000005,
            [
                "4000 0000 0000 0000",
                "4000 0000 0000 0001",
                "4000 0000 0000 0002",
                "4000 0000 0000 0003",
                "4000 0000 0000 0004",
                "4000 0000 0000 0005",
            ],
        ),
        (
            1234567890123450,
            1234567890123453,
            [
                "1234 5678 9012 3450",
                "1234 5678 9012 3451",
                "1234 5678 9012 3452",
                "1234 5678 9012 3453",
            ],
        ),
    ],
)
def test_card_number_generator(card_number_range, start, end, expected):
    generated_numbers = list(card_number_generator(start, end))
    assert generated_numbers == expected


# Тестирование генератора для крайних значений диапазона
def test_card_number_generator_edge_cases():
    # Генерация для одного номера
    generated_numbers = list(card_number_generator(4000000000000000, 4000000000000000))
    assert generated_numbers == ["4000 0000 0000 0000"]

    # Генерация для пустого диапазона
    generated_numbers = list(card_number_generator(4000000000000000, 3999999999999999))
    assert generated_numbers == []  # Ожидаем пустой список
