from firebase import firebase
from entities.user import User


class UserRepository:
    def __init__(self):
        self.db = firebase.FirebaseApplication(
            "https://gachapet-77d0f-default-rtdb.europe-west1.firebasedatabase.app/",
            None,
        )
        self.user = User()
        # result = self.db.get("/", None)
        # print(result)

    def put(self, user):
        result = self.db.post("/users", user)
        # print(result)

    def get_user(self, username):
        users = self.db.get("/users/", None)
        return users
        # print(users)

    def login(self, username, password):
        # Placeolder if
        if len(password) > 0:
            # Placeholder items data until firebase operations ready
            items = {"food": 6, "money": 10}
            self.user.set_user_data(username, password, items)
            return True
        return False
