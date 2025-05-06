import pygame
from spritesheet import SpriteSheet
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.settings = game.settings
        self.sprite_sheet = SpriteSheet("images/wilmoth.png")
        self.sprites = self.sprite_sheet.get_images(0,0,100,100,4)
        self.image = self.sprites[0]

        self.rect = self.image.get_rect()
        self.color = (255, 0, 255)

        self.rect.center = game.rect.center
        self.x = self.rect.x
        self.y = self.rect.y
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.frame = 0
        self.weapons = {
            "blaster" : 0,
            "big_sword": 0
        }

    def draw(self, game):
        

        pygame.draw.rect(game.screen, self.color, self.rect)

    def blit(self, game):
        self.image = self.sprites[self.frame]
        game.screen.blit(self.image, self.rect.topleft)

    def update(self):
        if self.game.frame_count % 5 == 0:
            self.frame = (self.frame + 1) % len(self.sprites)
        if self.moving_down:
            self.y += self.settings.PLAYER_SPEED
        if self.moving_up:
            self.y -= self.settings.PLAYER_SPEED
        if self.moving_left:
            self.x -= self.settings.PLAYER_SPEED
        if self.moving_right:
            self.x += self.settings.PLAYER_SPEED
        self.rect.topleft = (self.x, self.y)

