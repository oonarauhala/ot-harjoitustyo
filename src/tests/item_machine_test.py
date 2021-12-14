import unittest
from entities.item_machine import ItemMachine


class TestItemMachine(unittest.TestCase):
    def setUp(self):
        self.item_machine = ItemMachine()

    def test_item_machine_returns_real_item(self):
        item = self.item_machine.generate_item()
        self.assertIn(item, ["food", "money"])
