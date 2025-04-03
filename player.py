import pygame

class Player:
    def __init__(self, game):
        self.settings = game.settings
        
        self.rect = pygame.Rect(0,0,15,15)
        self.color = (255, 0, 255)

        self.rect.center = game.rect.center
        self.x = self.rect.x
        self.y = self.rect.y
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def draw(self, game):
        pygame.draw.rect(game.screen, self.color, self.rect)

    def update(self):
        if self.moving_down:
            self.y += self.settings.PLAYER_SPEED
        if self.moving_up:
            self.y -= self.settings.PLAYER_SPEED
        if self.moving_left:
            self.x -= self.settings.PLAYER_SPEED
        if self.moving_right:
            self.x += self.settings.PLAYER_SPEED
        self.rect.topleft = (self.x, self.y)

