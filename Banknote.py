class Banknote:
    existing_denominations = [1, 2, 5, 10, 20, 50, 100, 200]

    def __init__(self, banknote_denomination):
        self.__banknote_denomination = banknote_denomination

    def get_denomination(self):
        return self.__banknote_denomination
