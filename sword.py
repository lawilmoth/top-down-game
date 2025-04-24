import pygame 
import math 
from spritesheet import SpriteSheet
class Sword(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.settings = game.settings
        self.x = game.player.rect.centerx
        self.y = game.player.rect.centery
        self.sprite_sheet = SpriteSheet("images/sword.png")
        self.sprites = self.sprite_sheet.get_images(0,0,100,100,4)
        self.image = self.sprites[0]
        self.rect_size = self.settings.SWORD_RECT_SIZE
        self.rect = pygame.Rect(self.x,self.y, self.rect_size[0], self.rect_size[1])
        self.color = (255, 0, 0)

        self.rect.center = (self.x, self.y)

        self.direction = self.get_direction(game)

        self.left_images = []

        if self.direction[0] < 0:
            for sprite in self.sprites:
                
                self.left_images.append(pygame.transform.flip(sprite, True, False))

            self.sprites = self.left_images

        self.life_counter = 0
        self.frame = 0

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

    def blit(self, game):

        game.screen.blit(self.image, self.rect.topleft)
        

    
    def update(self, player):
        if self.life_counter % 3 == 0:
            self.frame = (self.frame + 1) % len(self.sprites)
            self.image = self.sprites[self.frame]
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

