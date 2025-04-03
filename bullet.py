import pygame 
import math 
class Bullet(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.settings = game.settings
        self.x = game.player.rect.centerx
        self.y = game.player.rect.centery
        self.rect = pygame.Rect(self.x,self.y,5,5)
        self.color = (255, 0, 0)

        self.rect.center = (self.x, self.y)

        self.direction = self.get_direction(game)

    def get_direction(self, game):
        mouse_at_fire = pygame.mouse.get_pos()
        distance = [
            mouse_at_fire[0] - game.player.x,
            mouse_at_fire[1] - game.player.y
        ]
        normalize = math.sqrt(distance[0]**2 + distance[1]**2)
        self.direction = [distance[0]/normalize, distance[1]/normalize]

        return self.direction

    def draw(self, game):
        pygame.draw.rect(game.screen, self.color, self.rect)

    
    def update(self):
        self.x += self.direction[0] * self.settings.BULLET_SPEED
        self.y += self.direction[1] * self.settings.BULLET_SPEED
        self.rect.topleft = (self.x, self.y)
