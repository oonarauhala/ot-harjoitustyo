class Pet:
    """A class for pet data.

    Attributes:
            name: Pet name.
            animal_type: Pet animal name.
            hunger: Pet hunger. 0 = not hungry.
    """

    def __init__(self):
        self.name = ""
        self.animal_type = ""
        self.hunger = 0

    def get_animal_type(self):
        return self.animal_type

    def is_hungry(self):
        """A function that tells whether pet is hungry or not.

        Returns:
                True if hunger is greater than 0.
                False if hunger is 0."""
        return self.hunger > 0

    def eat(self):
        """A function for decreasing pet hunger."""
        self.hunger -= 1

    def get_hungrier(self):
        """A function for increasing pet hunger."""
        self.hunger += 1

    def export_data(self):
        """A function for exporting pet data in json format for saving.

        Returns: A json object that includes all pet data.
        """
        return {"name": self.name, "type": self.animal_type, "hunger": self.hunger}

    def set_data(self, name, animal_type, hunger):
        self.name = name
        self.animal_type = animal_type
        self.hunger = hunger
