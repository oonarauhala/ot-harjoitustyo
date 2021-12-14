from random import choice


class ItemMachine:
    """A class that draws random items from a list."""

    def generate_item(self):
        """A function that draws random items from a list.

        Returns:
            The name of a random item."""
        return choice(["food", "money"])
