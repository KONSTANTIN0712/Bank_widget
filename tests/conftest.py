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
    return "**4301"

@pytest.fixture()
def number_account_len():
    return "Номер счета должен содержать 20 цифр"

@pytest.fixture()
def account_number_empty_line():
    return "Строка не может быть пустой"

@pytest.fixture()
def account_string_empty_line():
    return "Строка не может быть пустой"


@pytest.fixture()
def date_str():
    return "11.03.2024"

@pytest.fixture()
def date_str_empty_line():
    return "Строка не может быть пустой"

@pytest.fixture()
def filter_by_state():
    return "Строка не может быть пустой"

@pytest.fixture()
def sort_by_date_none():
    return "Отсутствует дата"