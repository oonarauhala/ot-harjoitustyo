from app import App
from entities import validator
from entities.user_repository import UserRepository
from entities.validator import Validator


def main():
    validator = Validator()
    users = UserRepository(validator)
    nimi = "Piko"
    user = {
        "password": "salasana",
        "items": {"food": 5, "money": 5},
    }
    users.put(nimi, user)
    print(users.get_user(nimi))
    # app = App()
    # app.run()


if __name__ == "__main__":
    main()
