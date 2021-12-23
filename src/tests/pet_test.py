import unittest
from entities.pet import Pet


class TestPet(unittest.TestCase):
    def setUp(self):
        self.pet = Pet()
        self.pet.set_data("Pottu", "dog", 3)

    def test_pet_get_animal_type_after_setting_data(self):
        animal_type = self.pet.get_animal_type()
        self.assertEqual(animal_type, "dog")

    def test_pet_is_hungry_after_setting_data(self):
        hunger = self.pet.is_hungry()
        self.assertEqual(hunger, True)

    def test_pet_not_hugry_after_eating_3_times(self):
        self.pet.eat()
        self.pet.eat()
        self.pet.eat()
        self.assertEqual(self.pet.is_hungry(), False)

    def test_pet_gets_hungrier(self):
        self.pet.get_hungrier()
        self.assertEqual(self.pet.hunger, 4)

    def test_pet_export_data(self):
        result = self.pet.export_data()
        self.assertEqual(result, {"name": "Pottu", "type": "dog", "hunger": 3})
