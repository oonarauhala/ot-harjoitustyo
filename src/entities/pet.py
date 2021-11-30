class Pet:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.hunger = 3

    def get_type(self):
        return self.animal_type

    def is_hungry(self):
        return True if self.hunger > 0 else False
