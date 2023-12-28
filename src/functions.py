from datetime import datetime
import json


def get_data(filename):
    with open(filename, encoding='utf-8') as operations_json:
        return json.load(operations_json)

def bank_acc(account):
    # возвращает True, если 'account' не пустое и содержит подстроку "Счет", иначе False
    return bool(account and "Счет" in account)

def bank_card(card):
    # возвращает True, если 'card' не пустое и не содержит подстроку "Счет", иначе False
    return bool(card and "Счет" not in card)

def hidden_card_num(card):
    # разделяет строку 'card' на название карты и номер
    card_name, card_number = card.rsplit(' ', 1)
    # маскируем номер карты, сохраняя видимыми первые 6 и последние 4 цифры
    visible_digits = card_number[:6] + '*' * 6 + card_number[-4:]
    # форматируем маскированный номер карты, группируя цифры по 4 с пробелами между группами
    formatted_number = ' '.join([visible_digits[i:i+4] for i in range(0, len(visible_digits), 4)])
    # возвращает строку, содержащую название карты и номер
    return f"{card_name} {formatted_number}"

def hidden_num_acc(account):
    # разделяет строку 'account' на название счёта и номер
    account_name, number_account = account.rsplit(' ', 1)
    # маскирует номер счёта, оставляя только последние 4 цифры
    return f"{account_name} {'*' * 2 + number_account[-4:]}"

def format_date(date):
    # убирает время, оставляя только дату в формате 'ГГГГ-ММ-ДД'
    short_date = date[:10]
    # конвертирует строку с датой в объект datetime и форматирует его в формат 'ДД.ММ.ГГГГ'
    return datetime.strptime(short_date, '%Y-%m-%d').strftime('%d.%m.%Y')
