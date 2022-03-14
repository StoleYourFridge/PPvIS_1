from Phone import Phone


class BankUser:
    def __init__(self, user_name, user_phone_bill, user_bank_card, user_storage):
        self.user_name = user_name
        self.user_phone = Phone(user_phone_bill)
        self.user_bank_card = user_bank_card
        self.user_storage = user_storage
