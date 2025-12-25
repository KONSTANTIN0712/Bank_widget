def get_mask_card_number(cart_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX"""
    if cart_number == "":
        return "Строка не может быть пустой"
    else:
        cart_number = str(cart_number)
        cart_number_no_spaces = cart_number.replace(" ", "")
        if len(cart_number_no_spaces) == 16:
            mask_number = (
                f"{cart_number_no_spaces[:-12]} {cart_number_no_spaces[-12:-10]}** **** {cart_number_no_spaces[-4:]}"
            )
            return mask_number
    return "Номер карты должен содержать 16 цифр"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))


def get_mask_account(cart_number: str) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX."""

    if cart_number == "":
        return "Строка не может быть пустой"
    else:
        cart_number = str(cart_number)
        cart_number_no_spaces = cart_number.replace(" ", "")
        if len(cart_number_no_spaces) == 20:
            mask_account = f"**{cart_number_no_spaces[-4:]}"
            return mask_account
        return "Номер счета должен содержать 20 цифр"


if __name__ == "__main__":
    print(get_mask_account("Счет 73654108430135874301"))
