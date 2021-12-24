from firebase import firebase


class UserRepository:
    """A class that handles all database and user data interactions.

    Attributes:
            database: Firebase dababase object with database url.
            user: A User data structure object where user data is saved during session.
            validator: A service that validates user input.
    """

    def __init__(self, validator, user):
        self.database = firebase.FirebaseApplication(
            "https://gachapet-77d0f-default-rtdb.europe-west1.firebasedatabase.app/",
            None,
        )
        self.user = user
        self.validator = validator

    def _put(self, name, user):
        self.database.post(f"/users/{name}", user)

    def _delete(self, name):
        self.database.delete("/users/", name)

    def _get_user(self, username):
        user = self.database.get(f"/users/{username}", None)
        return user

    def _user_exists(self, username):
        result = self._get_user(username)
        return True if result is not None else False

    def login(self, username, password):
        """A function for user login. Fetches data drom database.

        Args:
            username: User's handle name.
            password: User's password.

        Returns:
                True if user is found and password is correct.
                False if username not found and/or password is incorrect.
        """
        if self.validator.validate_string(username) and self.validator.validate_string(
            password
        ):
            if self._user_exists(username):
                user_data = self._get_user(username)
                id = self._parse_id(user_data)
                data = self._extract_by_id(user_data, id)
                if self._check_password(data["password"], password):
                    self.user.set_user_data(username, data["password"], data["items"])
                    return True
        return False

    def register(self, username, password):
        """A function for new user registration. Validates input strings.
        Saves username, password and default items locally in user-object.

        Args:
            username: Input username.
            password: Input password.

        Returns:
                True if inputs are valid and username does not exist.
                False if inputs are not valid or username already exists.
        """
        if self.validator.validate_string(username) and self.validator.validate_string(
            password
        ):
            if not self._user_exists(username):
                items = {"food": 5, "money": 5}
                self.user.set_user_data(username, password, items)
                return True
        return False

    def complete_registration(self, pet_name):
        """A function for saving pet name and user data in database.

        Args:
            pet_name: Input pet name.
        """
        self.user.pet.set_data(pet_name, "dog", 3)
        data = {
            "password": self.user.password,
            "items": {"food": self.user.food, "money": self.user.money},
            "pet": {
                "name": self.user.pet.name,
                "animal_type": self.user.pet.animal_type,
                "hunger": self.user.pet.hunger,
            },
        }
        self._put(self.user.name, data)

    def logout(self):
        """A function for user logout. Updates database with new user data and resets local user data."""
        self._delete(self.user.name)
        self._put(self.user.name, self.user.export_data())
        self.user.reset()

    def _parse_id(self, data):
        data_str = str(data)[2:22]
        return data_str

    def _extract_by_id(self, data, id):
        return data[id]

    def _check_password(self, correct_password, given_password):
        return correct_password == given_password
