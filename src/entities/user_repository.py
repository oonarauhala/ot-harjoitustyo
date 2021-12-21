from firebase import firebase
from entities.user import User


class UserRepository:
    def __init__(self, validator, user):
        self.db = firebase.FirebaseApplication(
            "https://gachapet-77d0f-default-rtdb.europe-west1.firebasedatabase.app/",
            None,
        )
        self.user = user
        self.validator = validator

    def _put(self, name, user):
        self.db.post(f"/users/{name}", user)

    def _get_user(self, username):
        users = self.db.get(f"/users/{username}", None)
        return users

    def login(self, username, password):
        if self.validator.validate_string(username) and self.validator.validate_string(
            password
        ):
            user_data = self._get_user(username)
            id = self._parse_id(user_data)
            data = self._extract_by_id(user_data, id)
            if self._check_password(data["password"], password):
                self.user.set_user_data(username, data["items"])
                return True
        return False

    def logout(self):
        self.user.reset()

    def _parse_id(self, data):
        data_str = str(data)[2:22]
        return data_str

    def _extract_by_id(self, data, id):
        return data[id]

    def _check_password(self, correct_password, given_password):
        return correct_password == given_password
