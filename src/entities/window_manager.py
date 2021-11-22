class WindowManager:
    def __init__(self, window):
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()

    def fill(self, colour):
        self.window.fill(colour)

    def show_pet(self, image):
        self.window.blit(image, (200, 100))
