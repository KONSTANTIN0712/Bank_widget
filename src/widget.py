from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_card: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    info_card_split = info_card.split(" ", 1)
    number_card = info_card
    print(info_card_split[0])
    if info_card_split[0] == "Счет":
        result = get_mask_account(number_card)
        return f"{info_card_split[0]} {result}"
    else:
        result = get_mask_card_number(number_card)
        return result


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 700079228960636"))


def get_date(date_str: str) -> str:
    """Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    new_date = f"{date_str[8:10]}.{date_str[5:7]}.{date_str[0:4]}"
    return new_date


if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))


# def mask_account_card(input_str: str) -> str:
#     parts = input_str.strip().split()
#     # Тип — первый элемент
#     type_word = parts[0]
#     # Остальная часть — номер
#     number_str = ' '.join(parts[1:])
#
#     # Извлечем только цифры
#     digits = ''.join(filter(str.isdigit, number_str))
#
#     if not digits:
#         return "Некорректный номер"
#
#     # Обработка для карт
#     if type_word.lower() != "счет":
#         # Проверка длины номера
#         if len(digits) != 16:
#             return "Некорректный номер карты"
#         masked_number = f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
#         return f"{type_word} {masked_number}"
#     else:
#         # Это счет
#         if len(digits) < 8:
#             return "Некорректный номер счета"
#         # Маскируем все внутренние цифры, кроме первых 4 и последних 4
#         num_inner_mask = '*' * (len(digits) - 8)
#         masked_number = f"{digits[:4]} {num_inner_mask} {digits[-4:]}"
#         return f"{type_word} {masked_number}"

# import re
#
# def mask_account_card(input_str: str) -> str:
#     # Определяем тип из входной строки
#     lower_input = input_str.lower()
#
#
#     # Ищем номер карты или счета (подразумеваем, что он есть в строке)
#     match_number = re.search(r'\b\d{13,19}\b', input_str)
#     if not match_number:
#         return "Номер не найден"
#
#     number_str = match_number.group()
#     digits = ''.join(filter(str.isdigit, number_str))
#     length = len(digits)
#
#     # Если в строке есть слово "счет" - маскируем как счет
#     if "счет" in lower_input:
#         # Маскировка для счета (скрыта часть, остается только последние 4)
#         if length < 4:
#             return "Некорректный номер счета"
#         return "**" + digits[-4:]
#     else:
#         # Маскировка для карты
#         # Стандартно у карт длина 13-19
#         if length < 13 or length > 19:
#             return "Некорректный номер карты"
#         start = digits[:6]  # первые 6 цифр
#         end = digits[-4:]    # последние 4 цифры
#         # Маскируем оставшиеся символы
#         middle_mask = '*' * (length - 10)
#         # Форматируем номер так, чтобы разбить на блоки по 4 (по желанию)
#         # Для примера сделаем так:
#         masked_number = (
#             f"{start[:4]} {start[4:]} {middle_mask} {end}"
#         )
#         return masked_number


if __name__ == "__main__":
    print(mask_account_card("Счет 73654108430135874305"))