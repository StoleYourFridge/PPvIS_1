from BanknotesStorage import BanknotesStorage
from BankCard import BankCard


class BankAccount:
    def __init__(self, account_bill, account_card, account_storage):
        self.account_bill = account_bill
        self.account_card: BankCard = account_card
        self.account_storage: BanknotesStorage = account_storage

    def get_banknotes_out_of_storage(self, required_storage):
        self.account_storage -= required_storage

    def get_banknotes_in_storage(self, addition_storage):
        self.account_storage += addition_storage

    def get_banknotes_out_of_bill(self, required_sum):
        self.account_bill -= required_sum

    def get_banknotes_in_bill(self, addition_storage):
        self.account_bill += addition_storage
