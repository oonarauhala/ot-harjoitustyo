from string import ascii_letters

VALID_CHARS = list(ascii_letters) + [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


class Validator:
    """A class for user input validation."""

    def validate_string(self, validation_string):
        """A function for checking if a tring meets input criteria.

        Args:
            validation_string: String to be validated.
        Returns:
                True if string is longer than 2 and consists of valid chars.
                False if string does not meet criteria."""
        if len(validation_string) > 2:
            for char in validation_string:
                if char not in VALID_CHARS:
                    return False
            return True
        return False
