from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_card: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    info_card_split = info_card.split()
    number_card = info_card_split[1]
    if info_card_split[0] =="Счет":
        result = get_mask_account(number_card)
    else:
        result = get_mask_card_number(number_card)
    return result

if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))



