import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("number, expected", [ ("7000 7922 8960 6361","7000 79** **** 6361"),
                                                   ("70007922 89606361","7000 79** **** 6361")])
def test_get_mask_card_number_space(number,expected) -> None:
    """Тесты для функции маскировки номера карты (работа кода с пробелами)"""
    assert get_mask_card_number(number) ==expected


def test_get_mask_card_number_len(number_card_len) -> None:
    """Тесты для функции маскировки номера карты (длина строки)"""
    assert get_mask_card_number(number_card_len) == "Номер карты должен содержать 16 цифр"


def test_get_mask_card_number_empty_line(number_card_empty_line):
    """Тесты для функции маскировки номера карты (пустая строка)"""
    assert get_mask_card_number(number_card_empty_line) == "Строка не может быть пустой"

@pytest.mark.parametrize("number, expected", [("736541084301 35874301", "**4301")])
def test_get_mask_account_space(number,expected) -> None:
    """Тесты для функции маскировки номера счета (работа кода с пробелами)"""
    assert get_mask_account(number) == expected


@pytest.mark.parametrize("number, expected", [("731654108430135874301", "Номер счета должен содержать 20 цифр"),
                                              ("7316541084135874301", "Номер счета должен содержать 20 цифр")])
def test_get_number_account_len(number, expected) -> None:
    """Тесты для функции маскировки номера счета (длина строки)"""
    assert get_mask_account(number) == expected




def test_get_number_account_empty_line(account_number_empty_line) -> None:
    """Тест пустой строки"""
    assert get_mask_account(account_number_empty_line) == "Строка не может быть пустой"