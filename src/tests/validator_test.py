import unittest
from entities.validator import Validator


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_correct_string(self):
        result = self.validator.validate_string("MyUsername")
        self.assertEqual(result, True)

    def test_string_too_short(self):
        result = self.validator.validate_string("aa")
        self.assertEqual(result, False)

    def test_string_contains_invalid_characters(self):
        result = self.validator.validate_string("AA%")
        self.assertEqual(result, False)
