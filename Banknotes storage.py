from Banknote import Banknote


class BanknotesStorage:
    def __init__(self, list_of_amounts):
        self.storage_banknotes = dict().fromkeys(Banknote.existing_denominations, list())
        for i in range(len(list_of_amounts)):
            example = Banknote(Banknote.existing_denominations[i])
            for j in range(list_of_amounts[i]):
                self.storage_banknotes[Banknote.existing_denominations[i]].append(example)
        self.bill_amount = self.refresh_bill_value()

    def refresh_bill_value(self):
        bill_value = 0
        for denomination in Banknote.existing_denominations:
            bill_value += len(self.storage_banknotes[denomination]) * denomination
        return bill_value

    def __lt__(self, other):
        for denomination in Banknote.existing_denominations:
            if len(self.storage_banknotes[denomination]) < len(other.storage_banknotes[denomination]):
                return False
        return True

    def __iadd__(self, other):
        for denomination in Banknote.existing_denominations:
            addition = Banknote(denomination)
            for index in range(len(other.storage_banknotes[denomination])):
                self.storage_banknotes[denomination].append(addition)
        self.bill_amount = self.refresh_bill_value()

    def __isub__(self, other):
        for denomination in Banknote.existing_denominations:
            for index in range(len(other.storage_banknotes[denomination])):
                self.storage_banknotes[denomination].pop()
        self.bill_amount = self.refresh_bill_value()

    def __str__(self):
        for denomination in Banknote.existing_denominations:
            print("With denomination {0} : {1} banknotes.".format(denomination,
                                                                  len(self.storage_banknotes[denomination])))
        print("Current storage bill : {}.".format(self.bill_amount))
