class BankCard:
    def __init__(self, card_password):
        self.__card_password = card_password
        self.__card_active = True

    def __eq__(self, other):
        if self.__card_password == other.__card_password:
            return True
        return False

    def get_card_password(self):
        return self.__card_password

    def set_activity_status(self, new_status):
        self.__card_active = new_status

    def get_activity_status(self):
        return self.__card_active
