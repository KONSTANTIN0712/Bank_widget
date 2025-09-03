def get_mask_card_number(cart_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX"""
    cart_number = str(cart_number)
    mask_number = f"{cart_number[:4]}  {cart_number[4:6]}** **** {cart_number[12:]}"
    return mask_number


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX."""


    account_number = str(account_number)
    mask_account = f"**{account_number[-4:]}"
    return mask_account


if __name__ == "__main__":
    print(get_mask_account(73654108430135874305))
