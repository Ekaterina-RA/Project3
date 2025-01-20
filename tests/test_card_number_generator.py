import pytest

from src.generators import card_number_generator


# Параметризованный тест для проверки корректных номеров карт
@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
    ],
)
def test_card_number_generator(start, end, expected):
    generated_numbers = list(card_number_generator(start, end))
    assert generated_numbers == expected


# Тестирование генератора для крайних значений диапазона
def test_card_number_generator_edge_cases():
    # Генерация для одного номера
    generated_numbers = list(card_number_generator(1, 1))
    assert generated_numbers == ["0000 0000 0000 0001"]

    # Генерация для пустого диапазона
    generated_numbers = list(card_number_generator(5, 4))
    assert generated_numbers == []  # Ожидаем пустой список
