from src.functions import bank_acc, bank_card, hidden_card_num, hidden_num_acc, format_date


def test_bank_acc():
    assert bank_acc("Карта 1234123412341234") is False
    assert bank_acc("Счет 12345678123456781234") is True
    assert bank_acc(None) is False

def test_bank_card():
    assert bank_card("Карта 1234123412341234") is True
    assert bank_card("Счет 12345678123456781234") is False
    assert bank_card(None) is False

def test_hidden_card_num():
    assert hidden_card_num("Карта 1234123412341234") == "Карта 1234 12** **** 1234"
    assert hidden_card_num("Visa Gold 8765432187654321") == "Visa Gold 8765 43** **** 4321"

def test_hidden_num_acc():
    assert hidden_num_acc("Счет 12345678123456781234") == "Счет **1234"

def test_format_date():
    assert format_date("2019-07-15T11:47:40.496961") == "15.07.2019"