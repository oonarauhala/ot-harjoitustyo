from entities.io import IO
from app import App
from entities.pet import Pet


def main():
    io = IO()
    pet = Pet("default_name", "default_type")
    app = App(io, pet)
    app.run()


if __name__ == "__main__":
    main()
