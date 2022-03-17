from BankEntity import BankUser, BankAccount
from BankCard import BankCard
from BanknotesStorage import BanknotesStorage
amount_of_attempts = 3


class Bank:
    def __init__(self):
        self.bank_accounts = list()
        self.bank_users = list()

    def system_creates_new_bank_account(self, bank_account, bank_user):
        self.bank_accounts.append(bank_account)
        self.bank_users.append(bank_user)

    def user_creates_new_bank_account(self):
        name = input("Please, enter your name : ")
        card_password = input("Please, enter your card password and remember it : ")
        start_bill = int(input("Please, enter bank account start bill : "))
        phone_start_bill = int(input("Please, enter phone start bill : "))
        print("Please, provide start bank account storage with banknotes : ")
        account_storage = BanknotesStorage.user_storage_input()
        print("Please, provide start user cash with banknotes : ")
        user_storage = BanknotesStorage.user_storage_input()
        account_card = BankCard(card_password, True)
        bank_account = BankAccount(start_bill, account_card, account_storage)
        bank_user = BankUser(name, phone_start_bill, account_card, user_storage)
        self.bank_accounts.append(bank_account)
        self.bank_users.append(bank_user)

    def usernames_output(self):
        for i in range(len(self.bank_users)):
            print("{0}){1}".format(i + 1, self.bank_users[i].name))

    def communicate_with_bank(self):
        while True:
            print("Enter 1) to add new user and bank account;")
            print("Enter 2) to work with existing users;")
            print("Enter 3) to finish the program;")
            choice = input("Input : ")
            if choice != '1' and choice != '2' and choice != '3':
                print("Well, ok")
                return
            if int(choice) == 1:
                self.user_creates_new_bank_account()
            elif int(choice) == 2:
                if len(self.bank_users) == 0:
                    print("There is no users to work with, enter somebody!")
                    continue
                self.usernames_output()
                user_number = int(input("Enter the number of user from {} existing you want to work with : ".format(
                                                                                          len(self.bank_users))))
                user_number -= 1
                if not self.bank_users[user_number].card.get_activity_status() and not self.bank_users[user_number].card.get_activity_status():
                    please = input("Sorry, this card is in stop-list, enter 'Please' to unlock : ")
                    if please == "Please":
                        self.bank_users[user_number].card.set_activity_status(True)
                        self.bank_accounts[user_number].card.set_activity_status(True)
                    else:
                        continue
                print("Please, enter user password : ")
                for attempt in range(amount_of_attempts, 0, -1):
                    user_password = input("{} attempts before card to be blocked : ".format(attempt))
                    if user_password == self.bank_users[user_number].card.get_card_password():
                        break
                else:
                    self.bank_users[user_number].card.set_activity_status(False)
                    self.bank_accounts[user_number].card.set_activity_status(False)
                    print("Congrats! You just successfully blocked the card!")
                    continue
                while True:
                    if user_number > len(self.bank_users):
                        continue
                    print("What do you want?")
                    print("Enter 0) to output users cash storage;")
                    print("Enter 1) to output phone bill;")
                    print("Enter 2) to output your bank account storage and bill data;")
                    print("Enter 3) to increase phone bill by your bank account;")
                    print("Enter 4) to increase your bank storage by user cash with banknotes;")
                    print("Enter 5) to increase your account bill by user cash with banknotes;")
                    print("Enter 6) to increase your user cash by storage banknotes;")
                    print("Enter 7) to increase your user cash by account bill banknotes;")
                    print("Enter 8) to finish robbery;")
                    account_action = int(input("Action number : "))
                    if account_action > 8 or account_action < 0:
                        continue
                    if account_action == 0:
                        print("Users cash : ")
                        self.bank_users[user_number].storage.output()
                    if account_action == 1:
                        print("Current phone bill : {}".format(self.bank_users[user_number].phone.get_phone_bill()))
                    elif account_action == 2:
                        print("Storage data : ")
                        self.bank_accounts[user_number].storage.output()
                        print("Account bill : {}".format(self.bank_accounts[user_number].bill))
                    elif account_action == 3:
                        print("Account bill : {}".format(self.bank_accounts[user_number].bill))
                        phone_increase = int(input("Enter the sum you want the phone bill to be increased by : "))
                        if phone_increase > self.bank_accounts[user_number].bill:
                            print("There is no such amount of money;")
                            continue
                        self.bank_users[user_number].phone.increase_phone_bill(phone_increase)
                        self.bank_accounts[user_number].get_banknotes_out_of_bill(phone_increase)
                    elif account_action == 4:
                        print("Please, enter banknotes amounts to insert them to storage : ")
                        addition = BanknotesStorage.user_storage_input()
                        if self.bank_users[user_number].storage < addition:
                            print("There is no such amount of banknotes, something gone wrong;")
                            continue
                        self.bank_accounts[user_number].get_banknotes_in_storage(addition)
                        self.bank_users[user_number].get_banknotes_out_of_storage(addition)
                    elif account_action == 5:
                        print("Please, enter banknotes amounts to insert them to account bill : ")
                        addition = BanknotesStorage.user_storage_input()
                        if self.bank_users[user_number].storage < addition:
                            print("There is no such amount of banknotes, something gone wrong;")
                            continue
                        self.bank_accounts[user_number].get_banknotes_in_bill(addition.bill_amount)
                        self.bank_users[user_number].get_banknotes_out_of_storage(addition)
                    elif account_action == 6:
                        print("Please, enter banknotes amounts to insert them to cash storage : ")
                        addition = BanknotesStorage.user_storage_input()
                        if self.bank_accounts[user_number].storage < addition:
                            print("There is no such amount of banknotes, something gone wrong;")
                            continue
                        self.bank_accounts[user_number].get_banknotes_out_of_storage(addition)
                        self.bank_users[user_number].get_banknotes_in_storage(addition)
                    elif account_action == 7:
                        addition = int(input("Please, enter amount of money you want to be inserted to users storage: "))
                        if addition > self.bank_accounts[user_number].bill:
                            print("There is no such amount of money, something gone wrong;")
                            continue
                        self.bank_accounts[user_number].get_banknotes_out_of_bill(addition)
                        self.bank_users[user_number].get_banknotes_in_storage(BanknotesStorage.decimal_to_storage(
                            addition))
                    elif account_action == 8:
                        break
            elif int(choice) == 3:
                print("Good bye!")
                return
