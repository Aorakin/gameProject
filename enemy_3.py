import pygame
import constants as c
import random
from item import Item
from bullet_enemy import Bulleten

class Enemy3(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy3,self).__init__()
        self.ing_explosion_01 = pygame.image.load('graphics/2_explo.png').convert_alpha()
        self.ing_explosion_01 = pygame.transform.scale(self.ing_explosion_01,(self.ing_explosion_01.get_width()*0.3,
                                                        self.ing_explosion_01.get_height()*0.3))
        self.ing_explosion_02 = pygame.image.load('graphics/2_explo2.png').convert_alpha()
        self.ing_explosion_02 = pygame.transform.scale(self.ing_explosion_02,(self.ing_explosion_02.get_width()*0.3,
                                                        self.ing_explosion_02.get_height()*0.3))
        self.ing_explosion_03 = pygame.image.load('graphics/2_explo3.png').convert_alpha()
        self.ing_explosion_03 = pygame.transform.scale(self.ing_explosion_03,(self.ing_explosion_03.get_width()*0.3,
                                                        self.ing_explosion_03.get_height()*0.3))
        self.ing_explosion_04 = pygame.image.load('graphics/2_explo4.png').convert_alpha()
        self.ing_explosion_04 = pygame.transform.scale(self.ing_explosion_04,(self.ing_explosion_04.get_width()*0.3,
                                                        self.ing_explosion_04.get_height()*0.3))
        self.ing_explosion_05 = pygame.image.load('graphics/2_explo5.png').convert_alpha()
        self.ing_explosion_05 = pygame.transform.scale(self.ing_explosion_05,(self.ing_explosion_05.get_width()*0.3,
                                                        self.ing_explosion_05.get_height()*0.3))
        self.ing_explosion_06 = pygame.image.load('graphics/2_explo6.png').convert_alpha()
        self.ing_explosion_06 = pygame.transform.scale(self.ing_explosion_06,(self.ing_explosion_06.get_width()*0.3,
                                                        self.ing_explosion_06.get_height()*0.3))
        self.changetim = 0
        self.imgtim1 = pygame.image.load('graphics/tim1.png').convert_alpha()
        self.imgtim2 = pygame.image.load('graphics/timr1.png').convert_alpha()
        self.imgtim3 = pygame.image.load('graphics/timr2.png').convert_alpha()
        self.imgtim4 = pygame.image.load('graphics/timr3.png').convert_alpha()
        self.imgtim5 = pygame.image.load('graphics/timl1.png').convert_alpha()
        self.imgtim6 = pygame.image.load('graphics/timl2.png').convert_alpha()
        self.imgtim7 = pygame.image.load('graphics/timl3.png').convert_alpha()

        self.anime_tim = [self.imgtim1,
                        self.imgtim2,
                        self.imgtim3,
                        self.imgtim4,
                        self.imgtim5,
                        self.imgtim6,
                        self.imgtim7]
        self.frametimmax = 10
        self.frametim = self.frametimmax


        self.image = self.anime_tim[self.changetim]


        self.destroyed = False
        self.invincible = False
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,c.DISPLAY_WIDTH-self.rect.width)
        self.rect.y = -self.rect.height
        self.frame_length_max = 6
        self.frame_length = self.frame_length_max

        self.hp = 10 #10
        self.bullets = pygame.sprite.Group()
        self.item = pygame.sprite.Group()
        self.bullet_timer_max = 50
        self.bullet_timer = self.bullet_timer_max
        self.states = {'FLY_DOWN' : 'FLY_DOWN',
                    'ATTACK' : 'ATTACK'}
        self.state = self.states['FLY_DOWN']
        self.init_state = True
        self.snd_hit = pygame.mixer.Sound('sound/hit.mp3')
        self.vel_x = 0
        self.vel_y = random.randrange(3,5)
        self.score_value = 40
        self.score = 0
        self.anime_explosion = [self.ing_explosion_01,
                                self.ing_explosion_02,
                                self.ing_explosion_03,
                                self.ing_explosion_04,
                                self.ing_explosion_05,
                                self.ing_explosion_06
                                ]

        self.anime_index = 0
        self.possition = [40,120,220]

    def update(self):
        self.bullets.update()
        self.item.update()
        #for bullet in self.bullets:
            # if bullet.rect.y <=0:
            #     self.bullets.remove(bullet)
        if self.state == 'FLY_DOWN':
            self.state_fly_down()
            self.rect.x +=self.vel_x
            self.rect.y +=self.vel_y
        elif  self.state == 'ATTACK':
            self.state_attack()
            self.rect.x +=self.vel_x
        for o in self.bullets:
            if o.rect.y >c.DISPLAY_HEIGHT+o.rect.height:
                self.bullets.remove(o)
        for j in self.item :
            if j.rect.y >c.DISPLAY_HEIGHT+j.rect.height+50:
                self.bullets.remove(j)
        if self.destroyed:
            
            max_index = len(self.anime_explosion)-1
            if self.frame_length ==0:
                if self.anime_index >= max_index  : 
                    for i in self.bullets:
                        for j in self.item:
                            if i.rect.y > c.DISPLAY_HEIGHT and j.rect.y > c.DISPLAY_HEIGHT:
                                print('kill have bu')
                                self.kill()
                        if i.rect.y>c.DISPLAY_HEIGHT and len(self.item)==0:
                            print('kill have bu without item')
                            self.kill()
                        
                    if len(self.bullets)==0:
                        for j in self.item:
                            if j.rect.y>c.DISPLAY_HEIGHT:
                                print('kill no bu')
                                self.kill()

                            
                else:
                    self.anime_index+=1
                    self.image = self.anime_explosion[self.anime_index]
                    self.frame_length = self.frame_length_max
                            
            else: 
                self.frame_length -=1
            
        else:
            self.image = self.anime_tim[self.changetim]      

    def state_fly_down(self):
        random.seed()
        # self.invincible = True
        randompos = random.choice(self.possition)
        if self.init_state:
            self.init_state = False
        if self.rect.y >=randompos:
            self.state = self.states['ATTACK']
            self.init_state = True


    def state_attack(self):

        if self.changetim>= len(self.anime_tim):
            self.changetim =0
        if self.init_state:
            self.vel_y = 0
            while self.vel_x == 0 :
                self.vel_x = random.randrange(-4,4)
            self.init_state = False
        if self.bullet_timer == 0 and not self.destroyed:
            self.shoot()
            # self.invincible = False
            self.bullet_timer = self.bullet_timer_max
        else :self.bullet_timer-=1
        if self.rect.x <=0:
            for i in range(1,4):
                   self.changetim = i
            self.vel_x *=-1
        elif self.rect.x + self.rect.width >=c.DISPLAY_WIDTH:
            for i in range(4,7):
                    self.changetim = i
            self.vel_x *=-1

    def shoot(self):
        new_bullet = Bulleten()
        new_bullet.vel_y = 4
        new_bullet.rect.x = self.rect.x +(self.rect.width//2)
        new_bullet.rect.y = self.rect.y + self.rect.height
        self.bullets.add(new_bullet)

    def genitem(self):
        random_change = random.randrange(1,100)
        if random_change >=1 and random_change<=15:
            item = Item(self.rect.x,self.rect.y,0,'graphics/item1.png')
            self.item.add(item)
        elif random_change>15 and random_change <=40:
            item = Item(self.rect.x,self.rect.y,1,'graphics/item2.png')
            self.item.add(item)
        elif random_change>40 and random_change <=55:
            item = Item(self.rect.x,self.rect.y,2,'graphics/item3.png')
            self.item.add(item)

    def get_hit(self):
        if not self.invincible:
            self.hp -=1  
            if self.hp <=0:
                self.invincible = True
                self.destroyed = True
                self.genitem()
                self.vel_x = 0
                self.vel_y = 0
                self.image = self.anime_explosion[self.anime_index]
            # else:
            #     self.hp -=1     
        else : 
            pass

            
      
        
