import pytest


@pytest.fixture()
def number_card_len():
    return ["700045655897954", "70004565589795412" ]

@pytest.fixture()
def number_card_empty_line():
    return ""


@pytest.fixture()
def account_number_empty_line():
    return ""

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
