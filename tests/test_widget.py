import pytest
from src.widget import mask_account_card, get_date

def test_mask_account_card() -> None:
    assert mask_account_card("MasterCard 7000792289606361") == "MasterCard 7000 79** **** 6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"


def test_mask_account_card_len() -> None:
    assert mask_account_card("MasterCard 7000792289606361321") == "Номер карты должен содержать 16 цифр"
    assert mask_account_card("Счет 73654108430135874305123") == "Номер счета должен содержать 20 цифр"

def test_mask_account_empty_line() -> None:
    assert mask_account_card("") == "Строка не может быть пустой"


def test_get_date(date_str) -> None:
    assert get_date("2024-03-11T02:26:18.671407") == date_str
    assert get_date("2024-03-11  T02:26:18.671407") == date_str

def test_get_date_empty_line(date_str_empty_line) -> None:
    assert get_date("") == date_str_empty_line