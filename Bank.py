import random
from BankEntity import BankUser, BankAccount
from BankCard import BankCard
from Banknote import Banknote


def generate_new_unique_value(set_of_existing_values, max_element_value, amount_of_elements):
    new_value = list()
    while len(new_value) == 0 or new_value in set_of_existing_values:
        new_value.clear()
        for index in range(amount_of_elements):
            new_value.append(random.random() % max_element_value)
    set_of_existing_values.add(new_value)
    return new_value


class Bank:
    def __init__(self):
        self.bank_accounts = dict()

    def system_creates_new_bank_account(self, bank_account, bank_user):
        self.bank_accounts.setdefault(bank_user, bank_account)

    def user_creates_new_bank_account(self):
        user_name = input("Please, enter your name : ")
        card_password = input("Please, enter your card password and remember it : ")
        account_start_bill = int(input("Please, enter bank account start bill : "))
        account_phone_start_bill = int(input("Please, enter phone start bill : "))
        account_banknotes_start_amount = Banknote.set_start_banknotes_amounts()
        account_card = BankCard(card_password, generate_new_unique_value(BankCard.card_id_individual_checker,
                                                                         max_id_element_value,
                                                                         card_id_length))
        account_id = generate_new_unique_value(BankAccount.account_id_individual_checker,
                                               max_id_element_value,
                                               account_id_length)
        bank_account = BankAccount(account_id, account_start_bill, account_card)
        bank_user = BankUser(user_name, account_phone_start_bill, account_card, account_banknotes_start_amount)
        self.bank_accounts.setdefault(bank_user, bank_account)



