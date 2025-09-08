from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_card: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    info_card_split = info_card.split(" ", 1)
    number_card = info_card
    if info_card_split[0] == "Счет":
        result = get_mask_account(number_card)
        return f"{info_card_split[0]} {result}"
    else:
        result = get_mask_card_number(number_card)
        return result


if __name__ == "__main__":
    print(mask_account_card("MasterCard 7158300734726758"))


def get_date(date_str: str) -> str:
    """Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    new_date = f"{date_str[8:10]}.{date_str[5:7]}.{date_str[0:4]}"
    return new_date


if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))
