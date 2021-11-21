class App:
    def __init__(self, io, pet):
        self.io = io
        self.pet = pet

    def run(self):
        while True:
            self.io.write("Give a name to your pet: ")
            name = self.io.ask()
            self.io.write("Choose your pet type (Cat/Dog):")
            pet_type = self.io.ask()
            self.pet.name = name
            self.pet.type = pet_type
            self.io.write(self.pet.get_type())
