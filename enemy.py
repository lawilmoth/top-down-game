import pygame
import random
import math 

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

        self.rect = pygame.rect.Rect(self.x, self.y, 20, 20)
        self.direction = (0, 0)
        self.hp = 2

    def update(self, player):
        
        self.target = player.rect.center
        distance = [
            self.target[0] - self.x,
            self.target[1] - self.y
        ]
        normalize = math.sqrt(distance[0]**2 + distance[1]**2)
        self.direction = [distance[0]/normalize, distance[1]/normalize]

        self.x += self.direction[0]
        self.y += self.direction[1]
        self.rect.topleft = (self.x, self.y)
    
    def draw(self, game):
        pygame.draw.rect(game.screen, self.color, self.rect)