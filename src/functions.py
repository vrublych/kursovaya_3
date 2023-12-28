from datetime import datetime
import json


def get_data(filename):
    with open(filename, encoding='utf-8') as operations_json:
        return json.load(operations_json)

def bank_acc(account):
    return bool(account and "Счет" in account)

def bank_card(card):
    return bool(card and "Счет" not in card)

def hidden_card_num(card):
    card_name, card_number = card.rsplit(' ', 1)
    visible_digits = card_number[:6] + '*' * 6 + card_number[-4:]
    formatted_number = ' '.join([visible_digits[i:i+4] for i in range(0, len(visible_digits), 4)])
    return f"{card_name} {formatted_number}"

def hidden_num_acc(account):
    account_name, number_account = account.rsplit(' ', 1)
    return f"{account_name} {'*' * 2 + number_account[-4:]}"

def format_date(date):
    short_date = date[:10]
    return datetime.strptime(short_date, '%Y-%m-%d').strftime('%d.%m.%Y')