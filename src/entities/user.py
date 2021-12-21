class User:
    def __init__(self):
        self.name = ""
        self.password = ""
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

    def set_user_data(self, username, password, items):
        self.name = username
        self.password = password
        self.food = items["food"]
        self.money = items["money"]

    def reset(self):
        self.name = ""
        self.password = ""
        self.food = 0
        self.money = 0

    def export_data(self):
        return {
            "password": self.password,
            "items": {"food": self.food, "money": self.money},
        }
