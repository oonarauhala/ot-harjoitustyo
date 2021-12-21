class User:
    def __init__(self):
        self.name = ""
        self.food = 0
        self.money = 0

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

    def set_user_data(self, username, items):
        self.name = username
        self.food = items["food"]
        self.money = items["money"]

    def reset(self):
        self.name = ""
        self.id = ""
        self.food = 0
        self.money = 0
