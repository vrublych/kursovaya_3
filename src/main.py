import os.path
from functions import get_data, bank_acc, bank_card, hidden_card_num, hidden_num_acc, format_date


def print_operation_details(operation):
    # вывод даты и описания операции
    print(format_date(operation.get("date", 0)), end=' ')
    print(operation.get('description'))

    # проверка и вывод скрытого номера счёта или карты
    if bank_acc(operation.get('from')):
        print(f"{hidden_num_acc(operation.get('from'))} ->", end=' ')
    elif bank_card(operation.get('from')):
        print(f"{hidden_card_num(operation.get('from'))} ->", end=' ')

    # проверка получателя и вывод скрытого номера счёта или карты
    if bank_acc(operation.get('to')):
        print(hidden_num_acc(operation.get('to')))
    elif bank_card(operation.get('to')):
        print(hidden_card_num(operation.get('to')))

    # вывод суммы операции и валюты
    print(operation['operationAmount']['amount'], end=' ')
    print(operation['operationAmount']['currency']['name'])
    print()

# путь к файлу с данными операций
if __name__ == "__main__":
    file = os.path.join("..", "operations.json")
    operations = get_data(file)
    # сортировка операций по дате в обратном порядке
    operations.sort(key=lambda d: d.get("date", '0'), reverse=True)

    # счётчик для вывода операций
    counter = 0
    for operation in operations:
        if operation.get('state') == 'EXECUTED':
            print_operation_details(operation)
            counter += 1
            if counter == 5:
                break
