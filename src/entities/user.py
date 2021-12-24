class User:
    """A class for keeping user data during a game session.

    Attributes:
            name: User name.
            password: User password.
            pet: Pet object associated with the user.
            food: Number of food user possesses.
            money: Number of money user possesses."""

    def __init__(self, pet):
        self.name = ""
        self.password = ""
        self.pet = pet
        self.food = 0
        self.money = 0

    def feed_pet(self, pet):
        """A function for feeding pet. Checks if pet is hungry before feeding.

        Args:
            pet: Pet to be fed.
        """
        self.food -= 1
        if pet.is_hungry():
            pet.eat()

    def recieve_item(self, item):
        """A function for increasing user items.

        Args:
            item: Name of item to be recieved.
        """
        if item == "food":
            self.food += 1
        elif item == "money":
            self.money += 1

    def pay(self):
        """A function for paying for a gacha game. Checks if user has money.

        Returns:
                True if user has enough money.
                False if user does not have enough money."""
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
        """A function for resetting user data."""
        self.name = ""
        self.password = ""
        self.food = 0
        self.money = 0

    def export_data(self):
        """A function for exporting user data in json format for saving.

        Returns: A json object that includes all user (& pet) data."""
        pet_data = self.pet.export_data()
        return {
            "password": self.password,
            "items": {"food": self.food, "money": self.money},
            "pet": pet_data,
        }
