import random
from BankCard import BankCard, card_id_length, max_id_element_value
from Banknote import Banknote


class BankAccount:
    account_id_individual_checker = set()

    def __init__(self, account_id, account_password, account_bill, account_cards):
        self.account_id = account_id
        self.account_password = account_password
        self.account_bill = account_bill
        self.account_cards = account_cards

    @staticmethod
    def generate_new_unique_value(set_of_existing_values, max_element_value, amount_of_elements):
        new_value = list()
        while len(new_value) == 0 or new_value in set_of_existing_values:
            new_value.clear()
            for index in range(amount_of_elements):
                new_value.append(random.random() % max_element_value)
        set_of_existing_values.add(new_value)
        return new_value

    def add_new_card_to_account(self, new_card_password):
        new_card = BankCard(new_card_password, BankAccount.generate_new_unique_value(BankCard.card_id_individual_checker,
                                                                                     max_id_element_value,
                                                                                     card_id_length))
        self.account_cards.append(new_card)

    def add_existing_card_to_account(self, card_password, card_id):
        new_card = BankCard(card_password, card_id)
        self.account_cards.append(new_card)






