from random import randint


class HungerGenerator:
    def generate_hunger(self):
        number = randint(0, 2000)
        if number == 0:
            return True
        return False