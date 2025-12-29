import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("expected", ["7000 79** **** 6361"])
def test_get_mask_card_number_space(number_card,expected) -> None:
    """Тесты для функции маскировки номера карты (работа кода с пробелами)"""
    assert get_mask_card_number(number_card) ==expected



def test_get_mask_card_number_len(number_card_len) -> None:
    """Тесты для функции маскировки номера карты (длина строки)"""
    assert get_mask_card_number(number_card_len) == "Номер карты должен содержать 16 цифр"


def test_get_mask_card_number_empty_line(number_card_empty_line):
    """Тесты для функции маскировки номера карты (пустая строка)"""
    assert get_mask_card_number(number_card_empty_line) == "Строка не может быть пустой"

@pytest.mark.parametrize("expected", ["**4301"])
def test_get_mask_account_space(number_account,expected) -> None:
    """Тесты для функции маскировки номера счета (работа кода с пробелами)"""
    assert get_mask_account(number_account) == expected



def test_get_number_account_len(account_number_len) -> None:
    """Тесты для функции маскировки номера счета (длина строки)"""
    assert get_mask_account(account_number_len) == "Номер счета должен содержать 20 цифр"



def test_get_number_account_empty_line(account_number_empty_line) -> None:
    """Тест пустой строки"""
    assert get_mask_account(account_number_empty_line) == "Строка не может быть пустой"