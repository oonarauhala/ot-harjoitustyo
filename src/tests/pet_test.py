import unittest
from unittest.mock import Mock
from entities.pet import Pet
from entities.user import User


class TestPet(unittest.TestCase):
    def setUp(self):
        self.pet = Pet("Pottu", "dog")

    def test_pet_init(self):
        self.assertEqual(self.pet.name, "Pottu")
        self.assertEqual(self.pet.animal_type, "dog")
        self.assertEqual(self.pet.hunger, 3)

    def test_pet_get_animal_type(self):
        animal_type = self.pet.get_animal_type()
        self.assertEqual(animal_type, "dog")

    def test_pet_is_hungry_after_init(self):
        hunger = self.pet.is_hungry()
        self.assertEqual(hunger, True)

    def test_pet_not_hugry_after_feeding_3_times(self):
        user = Mock(wraps=User())
        user.feed_pet(self.pet)
        user.feed_pet(self.pet)
        user.feed_pet(self.pet)
        self.assertEqual(self.pet.is_hungry(), False)

    def test_pet_gets_hungrier(self):
        self.pet.get_hungrier()
        self.assertEqual(self.pet.hunger, 4)
