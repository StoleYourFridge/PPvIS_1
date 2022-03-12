from typing import List


class Banknote:
    existing_denominations = [1, 2, 5, 10, 20, 50, 100, 200]

    def __init__(self, banknote_denomination):
        self.banknote_denomination = banknote_denomination

    def __add__(self, other):
        return self.banknote_denomination + other.banknote_denomination

    def __len__(self):
        return self.banknote_denomination

    def get_denomination(self):
        return self.banknote_denomination
