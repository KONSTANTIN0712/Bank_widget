from datetime import datetime
from typing import Dict, List


def filter_by_state(banking_operation: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]] | str:
    """функция принимает на вход список словарей и параметр сортировки,
    возвращает новый отсортированный список по параметру 'state'"""
    return [x for x in banking_operation if x["state"] == state]


def sort_by_date(banking_operation: List[Dict[str, str]]) -> List[Dict[str, str]] | str:
    """Функция принимает на вход список словарей и параметр порядка
    сортировки, возвращает новый список, в котором исходные словари
    отсортированы по дате"""
    for item in banking_operation:
        date_value = item.get("date")
        if date_value is None or date_value == "":
            return "Отсутствует дата"
    else:
        return sorted(banking_operation, key=lambda x: datetime.fromisoformat(x["date"]), reverse=True)


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ]
        )
    )

if __name__ == "__main__":
    print(
        sort_by_date(
            [
                {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ]
        )
    )
