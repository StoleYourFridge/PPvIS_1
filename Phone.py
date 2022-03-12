phone_length = 8


class Phone:
    phone_individual_checker = set()

    def __init__(self, phone_number, phone_bill):
        self.phone_number = phone_number
        self.phone_bill = phone_bill

    def increase_phone_bill(self, increase_value):
        self.phone_bill += increase_value

