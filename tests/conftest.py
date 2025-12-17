import pytest


@pytest.fixture()
def number_card():
    return "7000 79** **** 6361"

@pytest.fixture()
def number_card_len():
    return "Номер карты должен содержать 16 цифр"

@pytest.fixture()
def card_number_empty_line():
    return "Строка не может быть пустой"


@pytest.fixture()
def number_account():
    return "**7430"

@pytest.fixture()
def number_account_len():
    return "Номер счета должен содержать 19 цифр"

@pytest.fixture()
def account_number_empty_line():
    return "Строка не может быть пустой"