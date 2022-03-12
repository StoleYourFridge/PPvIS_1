account_id_length = 10


class BankAccount:
    account_id_individual_checker = set()

    def __init__(self, account_id, account_bill, account_card):
        self.account_id = account_id
        self.account_bill = account_bill
        self.account_card = account_card


