from random import choice


class ItemMachine:
    def generate_item(self):
        return choice(["food", "money"])
