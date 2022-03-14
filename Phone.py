class Phone:
    def __init__(self,  phone_bill):
        self.__phone_bill = phone_bill

    def increase_phone_bill(self, increase_value):
        self.__phone_bill += increase_value

    def get_phone_bill(self):
        return self.__phone_bill
