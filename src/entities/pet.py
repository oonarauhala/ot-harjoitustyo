class Pet:
    def __init__(self):
        self.name = ""
        self.animal_type = ""
        self.hunger = 0

    def get_animal_type(self):
        return self.animal_type

    def is_hungry(self):
        return True if self.hunger > 0 else False

    def eat(self):
        self.hunger -= 1

    def get_hungrier(self):
        self.hunger += 1

    def export_data(self):
        return {"name": self.name, "type": self.animal_type, "hunger": self.hunger}

    def set_data(self, name, animal_type, hunger):
        self.name = name
        self.animal_type = animal_type
        self.hunger = hunger
