class User:
    def __init__(self):
        self.food = 5
        self.money = 5

    def feed_pet(self, pet):
        self.food -= 1
        if pet.is_hungry():
            pet.eat()
