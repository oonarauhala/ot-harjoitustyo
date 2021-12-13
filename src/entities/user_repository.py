from firebase import firebase


class UserRepository:
    def __init__(self):
        self.db = firebase.FirebaseApplication(
            "https://gachapet-77d0f-default-rtdb.europe-west1.firebasedatabase.app/",
            None,
        )
        result = self.db.get("/", None)
        print(result)

    def put(self, user):
        result = self.db.post("/users", user)
        print(result)
