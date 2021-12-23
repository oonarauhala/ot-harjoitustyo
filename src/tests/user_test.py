import unittest
from entities.user import User
from entities.pet import Pet


class TestUser(unittest.TestCase):
    def setUp(self):
        self.pet = Pet()
        self.pet.set_data("Pottu", "dog", 3)
        self.user = User(self.pet)
        self.user.set_user_data("Nipsu", "aaaa", {"food": 5, "money": 5})

    def test_successful_feeding_pet_decreases_pet_hunger(self):
        self.user.feed_pet(self.pet)
        self.assertEqual(self.pet.hunger, 2)

    def test_successful_feeding_pet_decreases_food(self):
        self.user.feed_pet(self.pet)
        self.assertEqual(self.user.food, 4)

    def pet_not_hungry_feeding_doesnt_decrease_food(self):
        self.pet.hunger = 0
        self.user.feed_pet(self.pet)
        self.assertEqual(self.user.food, 5)

    def test_recieve_food_increases_food(self):
        self.user.recieve_item("food")
        self.assertEqual(self.user.food, 6)

    def test_recieve_money_increases_money(self):
        self.user.recieve_item("money")
        self.assertEqual(self.user.money, 6)
