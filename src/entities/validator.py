from string import ascii_letters

VALID_CHARS = list(ascii_letters) + [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


class Validator:
    def validate_string(self, username):
        if len(username) > 2:
            for char in username:
                if char not in VALID_CHARS:
                    return False
            return True
        return False
