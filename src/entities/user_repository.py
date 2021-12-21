from firebase import firebase
from entities.user import User


class UserRepository:
    def __init__(self, validator):
        self.db = firebase.FirebaseApplication(
            "https://gachapet-77d0f-default-rtdb.europe-west1.firebasedatabase.app/",
            None,
        )
        self.user = User()
        self.validator = validator

    def put(self, name, user):
        self.db.post(f"/users/{name}", user)

    def get_user(self, username):
        users = self.db.get(f"/users/{username}", None)
        return users

    def login(self, username, password):
        if self.validator.validate_string(username) and self.validator.validate_string(
            password
        ):
            # Placeholder items data until firebase operations ready
            items = {"food": 6, "money": 10}
            self.user.set_user_data(username, password, items)
            return True
        return False

    def logout(self):
        self.user = User()
