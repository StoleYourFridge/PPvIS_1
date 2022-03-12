import random

import BankCard
from Phone import Phone, phone_length
from BankCard import max_id_element_value
from BankAccount import BankAccount
from Banknote import Banknote


class BankUser:
    def __init__(self, user_name, user_account_password, user_phone_number, user_phone_bill, user_bank_cards,
                 user_banknotes):
        self.user_name = user_name
        self.user_account_password = user_account_password
        self.user_phone = Phone(user_phone_number, user_phone_bill)
        self.user_bank_cards = user_bank_cards
        self.user_banknotes = user_banknotes
        self.user_bill = self.refresh_user_bill(self.user_banknotes)

    @staticmethod
    def generate_unique_phone_number():
        return BankAccount.generate_new_unique_value(Phone.phone_individual_checker,
                                                     BankCard.max_id_element_value,
                                                     phone_length)

    def refresh_user_bill(self, user_banknotes):
        result = 0
        for denomination in Banknote.existing_denominations:
            result += denomination * self.user_banknotes[denomination]
        return result

