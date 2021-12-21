from entities import user
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

    def _delete(self, name):
        self.db.delete("/users/", name)

    def _get_user(self, username):
        user = self.db.get(f"/users/{username}", None)
        return user

    def _user_exists(self, username):
        result = self._get_user(username)
        return True if result != None else False

    def login(self, username, password):
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

    def logout(self):
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
