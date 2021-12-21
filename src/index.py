from app import App
from entities import validator
from entities.user_repository import UserRepository
from entities.validator import Validator
from entities.user import User


def main():
    user = User()
    validator = Validator()
    user_repository = UserRepository(validator, user)
    app = App(user_repository)
    app.run()


if __name__ == "__main__":
    main()
