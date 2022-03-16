from Phone import Phone
from BanknotesStorage import BanknotesStorage
from BankCard import BankCard


class BankUser:
    def __init__(self, user_name, user_phone_bill, user_bank_card, user_cash):
        self.user_name: str = user_name
        self.user_phone = Phone(user_phone_bill)
        self.user_bank_card: BankCard = user_bank_card
        self.user_cash: BanknotesStorage = user_cash

    def get_banknotes_in_cash(self, addition_storage):
        self.user_cash += addition_storage

    def get_banknotes_out_of_cash(self, required_storage):
        self.user_cash -= required_storage
