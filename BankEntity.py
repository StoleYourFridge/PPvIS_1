from BanknotesStorage import BanknotesStorage
from BankCard import BankCard
from Phone import Phone


class BankEntity:
    def __init__(self, card, storage):
        self.card: BankCard = card
        self.storage: BanknotesStorage = storage

    def get_banknotes_out_of_storage(self, required_storage):
        self.storage -= required_storage

    def get_banknotes_in_storage(self, addition_storage):
        self.storage += addition_storage


class BankAccount(BankEntity):
    def __init__(self, bill, card, storage):
        super().__init__(card, storage)
        self.bill: int = bill

    def get_banknotes_out_of_bill(self, required_sum):
        self.bill -= required_sum

    def get_banknotes_in_bill(self, addition_storage):
        self.bill += addition_storage


class BankUser(BankEntity):
    def __init__(self, name, phone_bill, card, storage):
        super().__init__(card, storage)
        self.name: str = name
        self.phone = Phone(phone_bill)
