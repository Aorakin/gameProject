import pygame
import constants as c
from bullet import Bullet
from bullet_2 import Bullet2
from bullet_3 import Bullet3
from hud import HUD
import math


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship,self).__init__()
        self.image = pygame.image.load('graphics/ship1.png').convert_alpha()
        # self.image = pygame.transform.scale(self.image,(self.image.get.width()*1.5,self.image.get.height()*1.5))
        self.img_ship02 = pygame.image.load('graphics/ship2.png').convert_alpha
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH//2
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height-49
        self.bullets = pygame.sprite.Group()
        self.snd_shoot = pygame.mixer.Sound('sound/shootsound.mp3')
        self.snd_shoot.set_volume(0.5)
        self.max_hp = 5
        self.lives = 4 
        self.hp = self.max_hp
        self.hud = HUD(self.max_hp,self.lives)
        self.hud_group = pygame.sprite.Group()
        self.hud_group.add(self.hud)
        self.invincible = False
        self.is_alive = True
        self.max_invincivle_timer = 80
        self.invincible_timer = 0
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.keys = pygame.key.get_pressed()
        self.snd_gethit = pygame.mixer.Sound('sound/kill2.mp3')
        # self.alpha_vel = 1

    def update(self):
        self.bullets.update()
        self.hud_group.update()
        for bullet in self.bullets:
            if bullet.rect.y <=0:
                self.bullets.remove(bullet)
        self.rect.x +=self.vel_x
        if self.rect.x <=0:
            self.rect.x=0
        elif self.rect.x >=c.DISPLAY_WIDTH - self.rect.width:
            self.rect.x = c.DISPLAY_WIDTH - self.rect.width
        self.rect.y +=self.vel_y

        #check invincibility
        if self.invincible_timer>0:
            self.invincible_timer -=1
        #     self.alpha_vel+=1
        # elif self.alpha_vel>=255:
        #     self.alpha_vel = 1

            
        else :
            self.invincible = False
            # self.image = self.image.set_alpha(1)
        #print(self.invincible)

    def shoot(self):
        if self.is_alive:
            self.snd_shoot.play()
            new_bullet = Bullet()
            new_bullet.rect.x = self.rect.x + (self.rect.width//2)-2
            new_bullet.rect.y = self.rect.y
            self.bullets.add(new_bullet)

    def shoot2way(self):
        if self.is_alive:
              self.snd_shoot.play()
              new_bu_right = Bullet2()
              new_bu_right.rect.x = self.rect.x + (self.rect.width)-9
              new_bu_right.rect.y = self.rect.y + 19
              new_bu_left = Bullet3()
              new_bu_left.rect.x = self.rect.x+5
              new_bu_left.rect.y = self.rect.y + 18
              self.bullets.add(new_bu_right)
              self.bullets.add(new_bu_left)

    def shoot3way(self):
        if self.is_alive:
            self.snd_shoot.play()
            new_bullet = Bullet()
            new_bullet.rect.x = self.rect.x + (self.rect.width//2)-2
            new_bullet.rect.y = self.rect.y
            new_bu_right = Bullet2()
            new_bu_right.rect.x = self.rect.x + (self.rect.width)-9
            new_bu_right.rect.y = self.rect.y + 19
            new_bu_left = Bullet3()
            new_bu_left.rect.x = self.rect.x+5
            new_bu_left.rect.y = self.rect.y + 18
            self.bullets.add(new_bullet)
            self.bullets.add(new_bu_right)
            self.bullets.add(new_bu_left)

    def get_hit(self):
        if self.is_alive:
            self.hp -= 1
            # print(self.wave())
            self.hud.health_bar.decrease_hp_value()
            self.snd_gethit.play()
            if self.hp <=0:
                self.hp = 0
                self.death()

        #print(f'HP = {self.hp}')

    def death(self):
        self.lives -=1
        #print(f"lives = {self.lives}")
        if self.lives<=0:
            self.lives=0
            self.is_alive = False
            self.image = pygame.Surface((0,0))
        self.hp=self.max_hp
        self.hud.health_bar.reset_hp_tomax()
        self.hud.lives.decrement_life()
        self.rect.x = c.DISPLAY_WIDTH//2
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height-49
        self.invincible = True
        self.invincible_timer = self.max_invincivle_timer
        # self.image = self.image.set_alpha(math.sin(self.alpha_vel))
        
    def increase_hp(self):
        #print(f'before increase {self.hp}')
        self.hud.health_bar.increase_hp_value()
        if self.hp<5:
            self.hp+=1
        # print(f'after increase {self.hp}')

    def wave(self):
        wave_value = math.sin(pygame.time.get_ticks())
        if wave_value>=0:
            return 255
        else:
            return 0 
       
       
        
 