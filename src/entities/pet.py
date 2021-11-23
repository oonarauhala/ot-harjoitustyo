class Pet:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.hunger = 0

    def get_type(self):
        return self.type

    def is_hungry(self):
        return True if self.hunger == 0 else False
