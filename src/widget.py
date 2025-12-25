from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_string: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""

    account_name = ""
    card_string = []

    if account_string == "":
        return "Строка не может быть пустой"
    else:
        for i in account_string:
            if i.isalpha():
                account_name += i
            elif i.isdigit():
                card_string.append(i)

    # После этого объединяем цифры в строку
    card_string_st = "".join(card_string)

    # Теперь можно использовать card_string_st в дальнейшем
    if account_string.startswith("Счет"):
        masked_number = get_mask_account(card_string_st)
        if masked_number == "Номер счета должен содержать 20 цифр":
            return "Номер счета должен содержать 20 цифр"
        else:
            return f"Счет {masked_number}"
    else:
        masked_card = get_mask_card_number(card_string_st)
        if masked_card == "Номер карты должен содержать 16 цифр":
            return "Номер карты должен содержать 16 цифр"
        else:
            return f"{account_name} {masked_card}"


if __name__ == "__main__":
    print(mask_account_card("Счет 73654108430135874305"))

if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))


def get_date(date_str: str) -> str:
    """Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    if date_str == "":
        return "Строка не может быть пустой"
    else:
        new_date = f"{date_str[8:10]}.{date_str[5:7]}.{date_str[0:4]}"
        return new_date


if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))

# if __name__ == "__main__":
#     print(mask_account_card("Счет 73654108430135874305"))

# account_name = ""
# card_string = []
# card_string_st = "".join(card_string)
#
# for i in account_string:
#     if i.isalpha():
#         account_name += i
# if account_string.startswith("Счет"):
#     return f"Счет {get_mask_account(card_string_st)}"
# else:
#     for i in account_string:
#         if i.isdigit():
#             card_string += str(i)
# masked_card = get_mask_card_number("".join(card_string))
# return account_name + " "+ masked_card
