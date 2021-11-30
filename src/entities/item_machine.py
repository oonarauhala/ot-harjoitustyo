import random


class ItemMachine:
    def generate_item(self):
        number = random.randint(1, 2)
        if number == 1:
            return "food"
        if number == 2:
            return "money"
