class Settings:
    def __init__(self):
        self.HEIGHT = 800
        self.WIDTH = 1000
        self.FPS = 60
        self.BULLET_SPEED = 10
        self.PLAYER_SPEED = 3
        self.PLAYER_RECT_SIZE = (15, 15)
        self.SWORD_RECT_SIZE = (self.PLAYER_RECT_SIZE[0]*6, self.PLAYER_RECT_SIZE[1]*6)

        self.SCALE_FACTOR = 1