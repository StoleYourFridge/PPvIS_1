class Banknote:
    existing_denominations = [1, 2, 5, 10, 20, 50, 100, 200]

    def __init__(self, banknote_denomination):
        self.__banknote_denomination = banknote_denomination

    def get_denomination(self):
        return self.__banknote_denomination

    @classmethod
    def set_start_banknotes_amounts(cls):
        banknotes = list()
        for current_denomination in cls.existing_denominations:
            current_amount = input("How much banknotes with {0} denomination you have : ".format(current_denomination))
            for i in range(int(current_amount)):
                banknotes.append(Banknote(current_denomination))
        return banknotes

