import pytest
from src.widget import mask_account_card, get_date

def test_mask_account_card() -> None:
    """Тест функции определяющей счет или карта и правильности маскировки"""
    assert mask_account_card("MasterCard 7000792289606361") == "MasterCard 7000 79** **** 6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"


def test_mask_account_card_len() -> None:
    """Тест определения корректности работы при некорректном количестве символов"""
    assert mask_account_card("MasterCard 7000792289606361321") == "Номер карты должен содержать 16 цифр"
    assert mask_account_card("Счет 73654108430135874305123") == "Номер счета должен содержать 20 цифр"


def test_mask_account_empty_line() -> None:
    """Тест корректности работы при пустой строке"""
    assert mask_account_card("") == "Строка не может быть пустой"


def test_get_date(date_str) -> None:
    """Тест корректности работы функции для работы с датой"""
    assert get_date(date_str) == "11.03.2024"


def test_get_date_empty_line(date_str_empty_line) -> None:
    """Тест корректности работы функции даты при пустой сроке"""
    "Строка не может быть пустой"
    assert get_date(date_str_empty_line) == "Строка не может быть пустой"