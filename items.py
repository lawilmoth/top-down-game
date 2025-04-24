from spritesheet import SpriteSheet
from pygame.sprite import Sprite
class Item(Sprite):
    def __init__(self, enemy):
        super().__init__()
        self.x = enemy.x
        self.y = enemy.y
        

    def update(self):
        
        self.current_frame = (self.current_frame + 1) % len(self.sprites)
        self.image = self.sprites[self.current_frame]

    def blit(self, game):
        self.image = self.sprites[self.current_frame]
        game.screen.blit(self.image, self.rect.topleft)



class Blaster(Item):
    def __init__(self, enemy):
        super().__init__(enemy)
        self.spritesheet = SpriteSheet("images/blaster1.png")
        self.sprites = self.spritesheet.get_images(0,0,100,100,20)
        self.current_frame = 0
        self.image = self.sprites[self.current_frame]

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def pickup(self, player):
        player.weapons.append("blaster")