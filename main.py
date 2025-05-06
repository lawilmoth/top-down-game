import pygame
from settings import Settings
from player import Player
from bullet import Bullet
from enemy import Enemy, BigEnemy
from sword import Sword, BigSword
import random, time
from level import Level
from items import Blaster, BigSwordItem

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


            if self.player.weapons["blaster"] > 0:
                blaster_count = self.player.weapons["blaster"]
               
                if blaster_count >= 100:
                    self._fire_bullet()
                elif self.frame_count % (100 - blaster_count) <= 0: 
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
        if self.player.weapons["big_sword"] >= 1:
            self.swords.add(BigSword(self))
        else:
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

        #Sword Damage
        collisions = pygame.sprite.groupcollide(self.swords, self.enemies, False, False)
        if collisions:
            enemies_hit = list(collisions.values())[0]
            sword = list(collisions.keys())[0]
            
            for enemy in enemies_hit:
                enemy.hp -= sword.damage
                enemy.knock_back(list(collisions.keys())[0])
                if enemy.hp <= 0:
                    self._handle_enemy_kill(enemy)
        
        pickup_up_item = pygame.sprite.spritecollideany(self.player, self.items)
        if pickup_up_item:
            if pickup_up_item.name == "blaster" or pickup_up_item.name == "big_sword":
                pickup_up_item.pickup(self.player)


    def _handle_enemy_kill(self, enemy):
        #Roll to drop a blaster
        if random.random() > .99:
            big_sword = BigSwordItem(enemy)
            self.items.add(big_sword)
        elif random.random() > .90:
            blaster = Blaster(enemy)
            self.items.add(blaster)
        enemy.kill()
        self.level.enemies_killed_this_round += 1
        self.score +=  game.level.enemy_points

game = Game()
game.run()