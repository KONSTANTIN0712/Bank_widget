import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number_space(number_card) -> None:
    """Тесты для функции маскировки номера карты (работа кода с пробелами)"""
    assert get_mask_card_number("7000792289606361") == number_card
    assert get_mask_card_number("7000 7922 8960 6361") == number_card
    assert get_mask_card_number("70007922 89606361") == number_card


def test_get_mask_card_number_len(number_card_len) -> None:
    """Тесты для функции маскировки номера карты (длина строки)"""
    assert get_mask_card_number("700045655897954") == number_card_len
    assert get_mask_card_number("700045655897954125") == number_card_len

def test_get_mask_card_number_empty_line(card_number_empty_line):
    """Тесты для функции маскировки номера карты (пустая строка)"""
    assert get_mask_card_number("") == card_number_empty_line


def test_get_mask_account_space(number_account) -> None:
    """Тесты для функции маскировки номера счета (работа кода с пробелами)"""
    assert get_mask_account("736541084301 3587430") == number_account
    assert get_mask_account("7365410 843013587430") == number_account
    assert get_mask_account("7365 410843013587430") == number_account


def test_get_number_account_len(number_account_len) -> None:
    """Тесты для функции маскировки номера счета (длина строки)"""
    assert get_mask_account("73654108430135874") == number_account_len
    assert get_mask_account("7365410843013587430123") == number_account_len


def test_get_number_account_empty_line(account_number_empty_line) -> None:
    assert get_mask_account("") == account_number_empty_line