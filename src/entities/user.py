class User:
    def __init__(self):
        self.food = 5
        self.money = 5

    def feed_pet(self, pet):
        self.food -= 1
        if pet.is_hungry():
            pet.eat()

    def recieve_item(self, item):
        if item == "food":
            self.food += 1
        elif item == "money":
            self.money += 1

    def pay(self):
        if self.money > 0:
            self.money -= 1
            return True
        return False
