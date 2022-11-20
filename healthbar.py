import pygame
import constants as c

class HealthBar(pygame.sprite.Sprite):
    def __init__(self,hp):
        super(HealthBar,self).__init__()
        self.max_hp = hp
        self.hp = self.max_hp
        #self.original_image = pygame.image.load('graphics/Health100.png').convert()
        self.imgtran = [pygame.image.load('graphics/Health100.png'),
                            pygame.image.load('graphics/Health90.png'),
                            pygame.image.load('graphics/Health80.png'),
                            pygame.image.load('graphics/Health70.png'),
                            pygame.image.load('graphics/Health60.png'),
                            pygame.image.load('graphics/Health50.png'),
                            pygame.image.load('graphics/Health40.png'),
                            pygame.image.load('graphics/Health30.png'),
                            pygame.image.load('graphics/Health20.png'),
                            pygame.image.load('graphics/Health10.png'),
                            pygame.image.load('graphics/Health0.png').convert()]
       
        self.minus = 0 
        self.image = self.imgtran[0]
        #self.image = self.original_image
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*0.25,self.image.get_height()*0.25))
        self.max_width = self.image.get_width()
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0
      

    def update(self):
        self.rect.x = self.vel_x
        self.rect.y = self.vel_y

    def increase_hp_value(self):
        if self.hp == self.max_hp or self.minus==0:
            pass
        else:
            #self.hp+=1
            self.minus-=2
            self.image = self.imgtran[self.minus]
            self.image = pygame.transform.scale(self.image,(self.image.get_width()*0.25,self.image.get_height()*0.25))
        

    def decrease_hp_value(self):
        self.hp-=1
        #reset hp
        # if self.hp<=0:
        #     self.minus=0
        #     self.hp = self.max_hp
        self.minus+=2
        #print(self.minus)
        self.image = self.imgtran[self.minus]
        
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*0.25,self.image.get_height()*0.25))
        
        # self.image = pygame.transform.scale(self.image,(self.max_width*self.hp//self.max_hp,self.rect.height))
        # x = self.rect.x
        # y = self.rect.y
        # self.rect = self.image.get_rect()
        # self.rect.x = x
        # self.rect.y = y

    def reset_hp_tomax(self):
        self.hp = self.max_hp
        self.minus =0
        self.image = self.imgtran[self.minus]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*0.25,self.image.get_height()*0.25))