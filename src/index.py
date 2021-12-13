from app import App
from entities.user_repository import UserRepository


def main():
    users = UserRepository()
    user = {
        "username": "Kayttajanimi",
        "password": "salasana",
        "items": {"food": 5, "money": 5},
    }
    app = App()
    app.run()


if __name__ == "__main__":
    main()
