import pygame
from settings import Settings
from player import Player
from bullet import Bullet
from enemy import Enemy, BigEnemy
from sword import Sword
import random, time
from level import Level
from items import Blaster

class Game:
    frame_count = 0
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
        self.items = pygame.sprite.Group()

        self.level = Level()

        #Initializes the font for the game
        pygame.font.init()
        self.font = pygame.font.SysFont("Comic Sans MS", 24)

        self.score = 0



    def run(self):
        while self.running:
            self._handle_events()
            self._handle_collisions()
            self.screen.fill((0,0,0))


            if self.frame_count % 4 == 0:   
                self._fire_bullet()
                #pass
            for bullet in self.bullets.sprites():
                if bullet.rect.left > self.settings.WIDTH or bullet.rect.right < 0:
                    bullet.kill()
                bullet.update()
                bullet.draw(self)

            for sword in self.swords.sprites():
                
                sword.update(self.player)
                sword.blit(self)
                if sword.life_counter > 15:
                    self.swords.remove(sword)
            
            self._spawn_enemy()
            self._update_enemies()

            
            if self.level.enemies_killed_this_round >= self.level.enemy_threshold and len(self.enemies) == 0:
                self._next_wave()


            self.player.update()
            
            self._update_screen()
            self.clock.tick(self.settings.FPS)
            self.frame_count +=1 
            
    def _swing_sword(self):
        self.swords.add(Sword(self))

    def _fire_bullet(self):
        self.bullets.add(Bullet(self))

    def _spawn_enemy(self):
        if random.random() < self.level.spawn_rate and self.level.enemy_count <= self.level.enemy_threshold:
            self.level.enemy_count+=1
            if random.random() > .1:
                self.enemies.add(Enemy(self))
            else:
                self.enemies.add(BigEnemy(self))

    def _update_enemies(self):
        for enemy in self.enemies.sprites():
            enemy.update(self.player, self.level)
            #enemy.draw(self)
            enemy.blit(self)

    def _next_wave(self):
        self.bullets.empty()
        self.enemies.empty()
        self.swords.empty()
        time.sleep(0.5)
        self.level.level_up()

    def _update_screen(self):
        self.player.blit(self)
        for item in self.items.sprites():
            item.update()
            item.blit(self)
        score_text = self.font.render(f"Score: {self.score}", False, (255,255,255))
        self.screen.blit(score_text, (0,0))
        pygame.display.flip()

    def _handle_events(self):
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

    def _handle_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, False)
        if collisions:    
            enemies_hit = list(collisions.values())[0]
            for enemy in enemies_hit:
                enemy.hp -= 1    
                enemy.knock_back(list(collisions.keys())[0])
                if enemy.hp <= 0:
                    self._handle_enemy_kill(enemy)

        collisions = pygame.sprite.groupcollide(self.swords, self.enemies, False, True)
        if collisions:
            number_of_enemies_killed = len(list(collisions.values())[0])
            self.level.enemies_killed_this_round += number_of_enemies_killed
            self.score += number_of_enemies_killed * game.level.enemy_points
        
        pickeup_up_item = pygame.sprite.spritecollideany(self.player, self.items)
        if pickeup_up_item:
            pickeup_up_item.kill()


    def _handle_enemy_kill(self, enemy):
        #Roll to drop a blaster
        if random.random() > .1:
            blaster = Blaster(enemy)
            self.items.add(blaster)
        enemy.kill()
        self.level.enemies_killed_this_round += 1
        self.score +=  game.level.enemy_points

game = Game()
game.run()