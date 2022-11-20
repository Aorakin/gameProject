import pygame
import constants as c
import random
import math
from item import Item
from bullet_enemy2 import Bulleten2
from bullet_enemy import Bulleten

class Enemy4(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy4,self).__init__()
        self.ing_explosion_01 = pygame.image.load('graphics/2_explo.png').convert_alpha()
        #self.ing_explosion_01 = pygame.transform.scale(self.ing_explosion_01,(self.ing_explosion_01.get_width()*0.3,
        #                                                self.ing_explosion_01.get_height()*0.3))
        self.ing_explosion_02 = pygame.image.load('graphics/2_explo2.png').convert_alpha()
        #self.ing_explosion_02 = pygame.transform.scale(self.ing_explosion_02,(self.ing_explosion_02.get_width()*0.3,
        #                                               self.ing_explosion_02.get_height()*0.3))
        self.ing_explosion_03 = pygame.image.load('graphics/2_explo3.png').convert_alpha()
        #self.ing_explosion_03 = pygame.transform.scale(self.ing_explosion_03,(self.ing_explosion_03.get_width()*0.3,
        #                                                self.ing_explosion_03.get_height()*0.3))
        self.ing_explosion_04 = pygame.image.load('graphics/2_explo4.png').convert_alpha()
        #self.ing_explosion_04 = pygame.transform.scale(self.ing_explosion_04,(self.ing_explosion_04.get_width()*0.3,
        #                                                self.ing_explosion_04.get_height()*0.3))
        self.ing_explosion_05 = pygame.image.load('graphics/2_explo5.png').convert_alpha()
        #self.ing_explosion_05 = pygame.transform.scale(self.ing_explosion_05,(self.ing_explosion_05.get_width()*0.3,
        #                                                self.ing_explosion_05.get_height()*0.3))

        self.image = pygame.image.load('graphics/boss1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*1.2,self.image.get_height()*1.2))
        self.destroyed = False
        self.invincible = False
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,c.DISPLAY_WIDTH-self.rect.width)
        self.rect.y = -self.rect.height
        self.frame_length_max = 6
        self.frame_length = self.frame_length_max
        self.bullet_timer_boss = [50,20]
        self.bullet_timer = [self.bullet_timer_boss[0],self.bullet_timer_boss[1]]
        self.hp = 120 #100
        self.snd_hit = pygame.mixer.Sound('sound/hit.mp3')
        self.bullets = pygame.sprite.Group()
        self.item = pygame.sprite.Group()
        self.vel_x = 1
        self.vel_y = 3
        self.score_value = 500 + (300 - ((pygame.time.get_ticks()//1000)-185))
        self.score = 0
        self.anime_explosion = [self.ing_explosion_01,
                                self.ing_explosion_02,
                                self.ing_explosion_03,
                                self.ing_explosion_04,
                                self.ing_explosion_05,
                                ]
       
        self.anime_index = 0
    def update(self):
        self.bullets.update()
        self.rect.x +=self.vel_x
        self.rect.y +=self.vel_y
        if self.rect.y >51 and self.vel_y!=0:
            self.vel_y=0
        for o in self.bullets:
            if o.rect.y >c.DISPLAY_HEIGHT:
                self.bullets.remove(o)
        # print(self.rect.y)
        # print(self.destroyed)
        for i in range(2):
            if self.bullet_timer[i] == 0 and not self.destroyed :
                if i ==0:self.shoot()
                else: self.shoot2()
                self.bullet_timer[i] = self.bullet_timer_boss[i]
            else: self.bullet_timer[i] -=1
        
        
        self.move()
        if self.destroyed:
            max_index = len(self.anime_explosion)-1
            if self.frame_length ==0:
                self.anime_index+=1
                if self.anime_index > max_index:
                    self.kill()
                else:
                    self.image = self.anime_explosion[self.anime_index]
                    self.frame_length = self.frame_length_max
            else: 
                self.frame_length -=1


    def move(self):
        if self.rect.x <=0 or self.rect.x + self.rect.width >=c.DISPLAY_WIDTH:
             self.vel_x *=-1
             self.vel_y+=1


    def shoot2(self):
        new_bullet3 = [Bulleten(),Bulleten()]
        new_bullet3[0].rect.x = self.rect.x +self.rect.width//2+10
        new_bullet3[1].rect.x = self.rect.x +self.rect.width//2-10
        for i in range(2):
            new_bullet3[i].rect.y = self.rect.y + self.rect.height
        new_bullet3[0].vel_x +=4
        new_bullet3[1].vel_x -=4
        self.bullets.add(new_bullet3)

    def shoot(self):
        new_bullet = Bulleten2()
        new_bullet2 = Bulleten2()
        new_bullet.rect.x = self.rect.x +self.rect.width -27
        new_bullet.rect.y = self.rect.y + self.rect.height -15
        new_bullet2.rect.x = self.rect.x +24
        new_bullet2.rect.y = self.rect.y + self.rect.height -15
        self.bullets.add(new_bullet)
        self.bullets.add(new_bullet2)

    def get_hit(self):
        if not self.invincible:
            self.hp -=1
            self.snd_hit.play()
            if self.hp <=0:
                self.invincible = True
                self.destroyed = True
                self.vel_x = 0
                self.vel_y = 0
                self.rect.x = self.rect.x-10
                self.rect.y = self.rect.y-10
                self.image = self.anime_explosion[self.anime_index]
            # else:
            
                

        else : 
            pass
    # def changetoi(self):
    #     self.rect_image2.x 
            
      
        
