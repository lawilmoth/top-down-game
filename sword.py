import pygame 
import math 

class Sword(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.settings = game.settings
        self.x = game.player.rect.centerx
        self.y = game.player.rect.centery

        self.rect_size = self.settings.SWORD_RECT_SIZE
        self.rect = pygame.Rect(self.x,self.y, self.rect_size[0], self.rect_size[1])
        self.color = (255, 0, 0)

        self.rect.center = (self.x, self.y)

        self.direction = self.get_direction(game)

        self.life_counter = 0

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

    
    def update(self, player):
        self.life_counter += 1
        if math.fabs(self.direction[0]) < math.fabs(self.direction[1]):
            #target up or down
            if self.direction[1] > 0:
                #target down
                self.rect.top = player.rect.bottom
            else: 
                #target up
                self.rect.bottom = player.rect.top
        
        else:
            #target left or right
            if self.direction[0] > 0:
                #target right
                self.rect.left = player.rect.right
            else: 
                #target left
                self.rect.right = player.rect.left

