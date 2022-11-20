import pygame
import constants as c
import random
from bullet_enemy import Bulleten

class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy2,self).__init__()
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
        self.change = 0
        self.imgtoi1 = pygame.image.load('graphics/toi.png').convert_alpha()
        self.imgtoi2 = pygame.image.load('graphics/toi2.png').convert_alpha()
        self.imgtoi3 = pygame.image.load('graphics/toi3.png').convert_alpha()
        self.imgtoi4 = pygame.image.load('graphics/toi4.png').convert_alpha()
        self.imgtoi5 = pygame.image.load('graphics/toi5.png').convert_alpha()

        self.anime_toi = [self.imgtoi1,
                        self.imgtoi2,
                        self.imgtoi3,
                        self.imgtoi4,
                        self.imgtoi5]
        self.frametoimax = 8
        self.frametoi = self.frametoimax


        self.image = self.anime_toi[self.change]
        #self.image = pygame.transform.scale(self.image,(self.image.get_width()*1,self.image.get_height()*1))

     
        # self.rect_image2 = self.image2[self.change].get_rect()
        self.destroyed = False
        self.invincible = False
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,c.DISPLAY_WIDTH-self.rect.width)
        self.rect.y = -self.rect.height
        self.frame_length_max = 6
        self.frame_length = self.frame_length_max

        self.hp = 5#5
        self.bullets = pygame.sprite.Group()
        self.item = pygame.sprite.Group()
        self.bullet_timer_toi = 60
        self.bullet_timer = self.bullet_timer_toi
        self.states = {'FLY_DOWN' : 'FLY_DOWN',
                    'ATTACK' : 'ATTACK',
                    'GOATTACK':'GOATTACK'}
        self.state = self.states['FLY_DOWN']
        self.init_state = True
        self.snd_hit = pygame.mixer.Sound('sound/hit.mp3')
        self.vel_x = 0
        self.vel_y = random.randrange(3,5)
        self.score_value = 10
        self.score = 0
        self.anime_explosion = [self.ing_explosion_01,
                                self.ing_explosion_02,
                                self.ing_explosion_03,
                                self.ing_explosion_04,
                                self.ing_explosion_05,
                                self.ing_explosion_06
                                ]

        self.anime_index = 0
        self.possition = [60,120,180,240,300,360,420]
        self.timeoftoi = pygame.time.get_ticks()

    def update(self):
        self.bullets.update()
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
        elif self.state == 'GOATTACK':
            self.state_fly_for_attack()
            self.rect.x += self.vel_x
            self.rect.y +=self.vel_y
        for o in self.bullets:
            if o.rect.y >c.DISPLAY_HEIGHT+o.rect.height:
                self.bullets.remove(o)

        if self.destroyed:
            max_index = len(self.anime_explosion)-1
            if self.frame_length ==0:
                if self.anime_index >= max_index  : 
                    for i in self.bullets:
                        if i.rect.y>c.DISPLAY_HEIGHT :
                            self.kill()
                        
                    if len(self.bullets)==0:
                            self.kill()
          
                else:
                    self.anime_index+=1
                    self.image = self.anime_explosion[self.anime_index]
                    self.frame_length = self.frame_length_max
            else: self.frame_length -=1
            
        else:
            self.image = self.anime_toi[self.change]
            
            
           

    def state_fly_down(self):
        random.seed()
        self.timeoftoi = pygame.time.get_ticks()
        randompos = random.choice(self.possition)
        if self.init_state:
            self.init_state = False
        if self.rect.y >=randompos:
            self.Y = self.rect.y
            self.state = self.states['ATTACK']
            self.init_state = True

    def state_fly_for_attack(self):
        if self.init_state:
            self.vel_x = 0
            self.Y = self.rect.y
            self.vel_y = random.randrange(5,10)
            self.init_state = False
        # if self.rect.y >= c.DISPLAY_HEIGHT-100:
        #    self.vel_y *= -1
        # elif self.rect.y < self.Y:
        #     self.vel_y = 0
        #     self.state = 'ATTACK'
        #     self.init_state = True
            
        

 

    def state_attack(self):
        if self.frametoi == 0:
            self.change+=1
            self.frametoi = self.frametoimax - abs(self.vel_x)
        else :self.frametoi -=1
        if self.change >= len(self.anime_toi):
            self.change =0
        if self.init_state:
            self.vel_y = 0
            while self.vel_x == 0 :
                self.vel_x = random.randrange(-5,5)
            self.init_state = False
        if self.bullet_timer == 0 and not self.destroyed:
            self.shoot()
            self.bullet_timer = self.bullet_timer_toi
        else :self.bullet_timer-=1
        if self.rect.x <=0 or self.rect.x + self.rect.width >=c.DISPLAY_WIDTH: self.vel_x *=-1
        if pygame.time.get_ticks() -self.timeoftoi >=5000: 
            self.state = self.states['GOATTACK']
            self.init_state = True

    def shoot(self):
        new_bullet = Bulleten()
        new_bullet.vel_y = 4
        new_bullet.rect.x = self.rect.x +(self.rect.width//2)
        new_bullet.rect.y = self.rect.y + self.rect.height
        self.bullets.add(new_bullet)

    def get_hit(self):
        if not self.invincible:
            self.hp -=1  
            if self.hp <=0:
                self.invincible = True
                self.destroyed = True
                self.vel_x = 0
                self.vel_y = 0
                self.image = self.anime_explosion[self.anime_index]
            # else:
            #     self.hp -=1     
        else : 
            pass
    def speedup_en2(self):
        self.vel_y+=0.2

            
      
        