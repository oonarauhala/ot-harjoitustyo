import unittest
from entities.user import User
from entities.pet import Pet


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_init(self):
        self.assertEqual(self.user.food, 5)
        self.assertEqual(self.user.money, 5)

    def test_successful_feeding_pet_decreases_pet_hunger(self):
        pet = Pet("Pottu", "dog")
        self.user.feed_pet(pet)
        self.assertEqual(pet.hunger, 2)

    def test_successful_feeding_pet_decreases_food(self):
        pet = Pet("Pottu", "dog")
        self.user.feed_pet(pet)
        self.assertEqual(self.user.food, 4)

    def pet_not_hungry_feeding_doesnt_decrease_food(self):
        pet = Pet("Pottu", "dog")
        pet.hunger = 0
        self.user.feed_pet(pet)
        self.assertEqual(self.user.food, 5)

    def test_recieve_food_increases_food(self):
        self.user.recieve_item("food")
        self.assertEqual(self.user.food, 6)

    def test_recieve_money_increases_money(self):
        self.user.recieve_item("money")
        self.assertEqual(self.user.money, 6)
