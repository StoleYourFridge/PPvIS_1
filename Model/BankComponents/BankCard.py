DEFAULT_AMOUNT_OF_STEPS = 3


class BankCard:
    def __init__(self,
                 card_password: str,
                 before_being_blocked_situation: bool,
                 steps_before_being_blocked: int):
        self.card_password = str(card_password)
        self.before_being_blocked_situation = before_being_blocked_situation
        self.steps_before_being_blocked = steps_before_being_blocked

    def get_card_password(self):
        return self.card_password

    def get_before_being_blocked_situation(self):
        return self.before_being_blocked_situation

    def get_steps_before_being_blocked(self):
        return self.steps_before_being_blocked

    def set_before_being_blocked_situation(self,
                                           before_blocked: bool):
        self.before_being_blocked_situation = before_blocked

    def set_steps_to_default(self):
        self.steps_before_being_blocked = DEFAULT_AMOUNT_OF_STEPS

    def increase_steps(self):
        self.steps_before_being_blocked += 1

    def decrease_steps(self):
        self.steps_before_being_blocked -= 1
