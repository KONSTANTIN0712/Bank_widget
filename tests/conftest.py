import pytest


@pytest.fixture()
def number_card():
    return "7000 7922 8960 6361"


@pytest.fixture()
def number_card_len():
    return ["700045655897954"]

@pytest.fixture()
def number_card_empty_line():
    return ""


@pytest.fixture()
def number_account():
    return "736541084301 35874301"

@pytest.fixture()
def account_number_len():
    return "73654108430135874"

@pytest.fixture()
def account_number_empty_line():
    return ""

@pytest.fixture()
def account_string_empty_line():
    return "Строка не может быть пустой"


@pytest.fixture()
def date_str():
    return "2024-03-11T02:26:18.671407"

@pytest.fixture()
def date_str_empty_line():
    return ""



@pytest.fixture()
def sort_date_none():
    return ([{'id': 41428829, 'state': 'EXECUTED', 'date': ''},
                         {'id': 615064591, 'state': 'CANCELED', 'date': ''},
                         {'id': 594226727, 'state': 'CANCELED', 'date': ''},
                         {'id': 939719570, 'state': 'EXECUTED', 'date': ''}])
