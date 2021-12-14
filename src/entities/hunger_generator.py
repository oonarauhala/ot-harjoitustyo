from random import randint


class HungerGenerator:
    """A class that randomly generates hunger for a pet. A number is randomly chosen from
    range 0-2000 and checked if it is zero.
    """

    def generate_hunger(self):
        """A function that draws a radom number from range 0-2000.

        Returns:
            True, if drawn number is zero.
            False, if drawn number is any other than zero.
        """
        number = randint(0, 2000)
        if number == 0:
            return True
        return False
