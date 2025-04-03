import pygame
from settings import Settings
settings = Settings()

class SpriteSheet():
    SS_GAP = 16
    SS_REFERENCE = (0, 0)
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()
        self.sprite_sheet.set_colorkey((0, 0, 0))
        

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width * settings.SCALE_FACTOR, height * settings.SCALE_FACTOR))
        image.set_colorkey((0, 0, 0))
        image.convert_alpha()
        return image
    
    def get_images(self, xi, yi, width, height, number_of_frames):
        return [self.get_image(
            xi + i*self.SS_GAP, 
            yi, 
            width, 
            height) 
            for i in range(number_of_frames)]
    