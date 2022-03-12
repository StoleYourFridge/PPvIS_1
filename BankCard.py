card_id_length = 8
max_id_element_value = 10


class BankCard:
    card_id_individual_checker = set()

    def __init__(self, card_password, card_id):
        self.__card_password = list(card_password)
        self.__card_id = card_id
        self.__card_active = True

    def __eq__(self, other):
        if self.__card_id == other.__card_id and self.__card_password == other.__card_password:
            return True
        return False

    def get_card_password(self):
        return self.__card_password

    def get_card_id(self):
        return self.__card_id

    def get_activity_status(self):
        return self.__card_active
