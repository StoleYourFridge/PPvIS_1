from Phone import Phone


class BankUser:
    def __init__(self, user_name, user_phone_bill, user_bank_card, user_banknotes):
        self.user_name = user_name
        self.user_phone = Phone(user_phone_bill)
        self.user_bank_card = user_bank_card
        self.user_banknotes = user_banknotes
        self.user_bill = self.refresh_user_bill(self.user_banknotes)

    def refresh_user_bill(self, user_banknotes):
        result = 0
        for i in range(len(self.user_banknotes)):
            result += user_banknotes[i].get_denomination()
        return result
