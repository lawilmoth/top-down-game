import pygame
import random
import math
from spritesheet import SpriteSheet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.settings = game.settings
        spawn = random.choice(["top","bottom", "left", "right"])
        if spawn == "top":
            self.x = random.randint(0, self.settings.WIDTH)
            self.y = 0
        if spawn == "bottom":
            self.x = random.randint(0, self.settings.WIDTH)
            self.y = self.settings.HEIGHT
        if spawn == "right":
            self.x = self.settings.WIDTH
            self.y = random.randint(0, self.settings.HEIGHT)
        if spawn == "left":
            self.x = 0
            self.y = random.randint(0, self.settings.HEIGHT)


        self.color = (55, 50, 255)

        self.spritesheet = SpriteSheet("images/enemy.png")
        self.sprites = self.spritesheet.get_images(0,0,100,100,6)
        self.image = self.sprites[0]

        self.rect = self.image.get_rect()
        self.direction = (0, 0)
        self.hp = 2
        self.frame = 0
        self.frame_count = 0 

    def update(self, player, level):
        self.frame_count += 1 
        if self.frame_count % 5 == 0:
            self.frame += 1 
            if self.frame == len(self.sprites):
                self.frame = 0
        self.target = player.rect.center
        distance = [
            self.target[0] - self.x,
            self.target[1] - self.y
        ]
        normalize = math.sqrt(distance[0]**2 + distance[1]**2)
        self.direction = [distance[0]/normalize, distance[1]/normalize]

        self.x += (self.direction[0] * level.enemy_speed_multiplier)
        self.y += (self.direction[1] * level.enemy_speed_multiplier)
        self.rect.topleft = (self.x, self.y)
    
    def draw(self, game):
        pygame.draw.rect(game.screen, self.color, self.rect)

    def blit(self, game):
        self.image = self.sprites[self.frame]
        game.screen.blit(self.image, self.rect.topleft)
        