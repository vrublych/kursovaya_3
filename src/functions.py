from datetime import datetime
import json


def get_data(filename):
    operations_json = open(filename, encoding='utf-8')
    return json.load(operations_json)

def bank_acc(account):
    return bool(account and "Счет" in account)

def bank_card(card):
    return bool(card and "Счет" not in card)

def hidden_card_num(card):
    card_list = card.split(' ')
    card_name = ' '.join(card_list[:-1])
    number_card = card_list[-1]
    number = list(number_card)
    for x in range(6, 12):
        number[x] = '*'
    number.insert(4, ' ')
    number.insert(9, ' ')
    number.insert(14, ' ')
    return f"{card_name} {''.join(number)}"

def hidden_num_acc(account):
    account_name, number_account = account.rsplit(' ', 1)
    return f"{account_name} {'*' * 2 + number_account[-4:]}"

def format_date(date):
    short_date = date[:10]
    return datetime.strptime(short_date, '%Y-%m-%d').strftime('%d.%m.%Y')