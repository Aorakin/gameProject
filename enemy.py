import pygame
import constants as c
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
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

        self.image = pygame.image.load('graphics/mons.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*0.85,self.image.get_height()*0.85))
        self.image2 = [pygame.image.load('graphics/toi.png'),pygame.image.load('graphics/toi2.png'),pygame.image.load('graphics/toi3.png'),pygame.image.load('graphics/toi4.png'),pygame.image.load('graphics/toi5.png'),
        pygame.image.load('graphics/toi.png'),pygame.image.load('graphics/toi2.png'),pygame.image.load('graphics/toi3.png'),pygame.image.load('graphics/toi4.png'),pygame.image.load('graphics/toi5.png'),
        pygame.image.load('graphics/toi.png'),pygame.image.load('graphics/toi2.png'),pygame.image.load('graphics/toi3.png'),pygame.image.load('graphics/toi4.png'),pygame.image.load('graphics/toi5.png').convert_alpha()]
        self.change = 0
        self.rect_image2 = self.image2[self.change].get_rect()
        self.destroyed = False
        self.invincible = False
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,c.DISPLAY_WIDTH-self.rect.width)
        self.rect.y = -self.rect.height
        self.frame_length_max = 6
        self.frame_length = self.frame_length_max

        self.hp = 3
        self.snd_hit = pygame.mixer.Sound('sound/kill2.mp3')
        self.vel_x = 0
        self.vel_y = random.randrange(3,8)
        self.vel2_x = 0
        self.vel2_y = random.randrange(3,8)
        self.score = 0
        self.anime_explosion = [self.ing_explosion_01,
                                self.ing_explosion_02,
                                self.ing_explosion_03,
                                self.ing_explosion_04,
                                self.ing_explosion_05,
                                ]

        self.anime_index = 0
    def update(self):
        self.rect.x +=self.vel_x
        self.rect.y +=self.vel_y
        self.rect_image2.x +=self.vel2_x
        self.rect_image2.y +=self.vel2_y
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

    def get_hit(self):
        if not self.invincible:
            self.hp -=1
            if self.hp <=0:
                self.destroyed = True
                self.invincible = True
                self.snd_hit.play()
                self.rect.x = self.rect.x-10
                self.rect.y = self.rect.y-10
                self.image = self.anime_explosion[self.anime_index]
        else : 
            pass
    # def changetoi(self):
    #     self.rect_image2.x 
            
      
        