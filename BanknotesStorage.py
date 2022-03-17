from Banknote import Banknote


class BanknotesStorage:
    def __init__(self, list_of_amounts):
        self.storage_banknotes = dict().fromkeys(Banknote.existing_denominations)
        for i in range(len(list_of_amounts)):
            self.storage_banknotes[Banknote.existing_denominations[i]] = list()
            for j in range(list_of_amounts[i]):
                example = Banknote(Banknote.existing_denominations[i])
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
                return True
        return False

    def __iadd__(self, other):
        for denomination in Banknote.existing_denominations:
            addition = Banknote(denomination)
            for index in range(len(other.storage_banknotes[denomination])):
                self.storage_banknotes[denomination].append(addition)
        self.bill_amount = self.refresh_bill_value()
        return self

    def __isub__(self, other):
        for denomination in Banknote.existing_denominations:
            for index in range(len(other.storage_banknotes[denomination])):
                self.storage_banknotes[denomination].pop()
        self.bill_amount = self.refresh_bill_value()
        return self

    def output(self):
        for denomination in Banknote.existing_denominations:
            print("With denomination {0} : {1} banknotes.".format(denomination,
                                                                  len(self.storage_banknotes[denomination])))
        print("Current storage bill : {}.".format(self.bill_amount))

    @staticmethod
    def decimal_to_storage(bill_to_get_out):
        denomination_amounts = list()
        Banknote.existing_denominations.reverse()
        for current_denomination in Banknote.existing_denominations:
            current_banknotes_amount = bill_to_get_out // current_denomination
            bill_to_get_out -= current_banknotes_amount * current_denomination
            denomination_amounts.append(current_banknotes_amount)
        denomination_amounts.reverse()
        Banknote.existing_denominations.reverse()
        return BanknotesStorage(denomination_amounts)

    @staticmethod
    def user_storage_input():
        denomination_amounts = list()
        for denomination in Banknote.existing_denominations:
            current_amount = int(input("Amount of banknotes with {} denomination : ".format(denomination)))
            denomination_amounts.append(current_amount)
        return BanknotesStorage(denomination_amounts)
