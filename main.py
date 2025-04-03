import pygame
from settings import Settings
from player import Player
from bullet import Bullet
from enemy import Enemy
from sword import Sword
import random 


class Game:
    def __init__(self):
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.settings.WIDTH, self.settings.HEIGHT)
        )
        self.rect = self.screen.get_rect()
        pygame.display.set_caption("My Game")
        self.running = True

        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.swords = pygame.sprite.Group()



    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.player.moving_left = True
                    if event.key == pygame.K_d:
                        self.player.moving_right = True
                    if event.key == pygame.K_w:
                        self.player.moving_up = True
                    if event.key == pygame.K_s:
                        self.player.moving_down = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.player.moving_left = False
                    if event.key == pygame.K_d:
                        self.player.moving_right = False
                    if event.key == pygame.K_w:
                        self.player.moving_up = False
                    if event.key == pygame.K_s:
                        self.player.moving_down = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._swing_sword()


            collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
            collisions = pygame.sprite.groupcollide(self.swords, self.enemies, False, True)

    
            self.screen.fill((0,0,0))

            #self._fire_bullet()
            for bullet in self.bullets.sprites():
                if bullet.rect.left > self.settings.WIDTH or bullet.rect.right < 0:
                    bullet.kill()
                bullet.update()
                bullet.draw(self)

            for sword in self.swords.sprites():
                
                sword.update(self.player)
                sword.draw(self)
                if sword.life_counter > 15:
                    self.swords.remove(sword)
            
            
            if random.random() > .80:
                self.enemies.add(Enemy(self))
            for enemy in self.enemies.sprites():
                enemy.update(self.player)
                enemy.draw(self)

            self.player.update()
            self.player.draw(self)
            



            pygame.display.flip()
            self.clock.tick(self.settings.FPS)
            
    def _swing_sword(self):
        self.swords.add(Sword(self))

    def _fire_bullet(self):
        self.bullets.add(Bullet(self))

game = Game()
game.run()