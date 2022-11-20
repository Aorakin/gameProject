import pygame
import constants as c

class Bulleten2(pygame.sprite.Sprite):
    def __init__(self):
        super(Bulleten2,self).__init__()
        self.width = 4
        self.height = self.width+3
        self.size = (self.width,self.height)
        self.bu1 = pygame.image.load('graphics/buen1.png').convert()
        self.bu1 =pygame.transform.scale(self.bu1,(self.bu1.get_width()*0.8,self.bu1.get_height()*0.7))
        self.bu2 =pygame.image.load('graphics/buen2.png').convert()
        self.bu2 =pygame.transform.scale(self.bu2,(self.bu2.get_width()*0.8,self.bu2.get_height()*0.7))
        self.bu3 = pygame.image.load('graphics/buen3.png').convert()
        self.bu3 =pygame.transform.scale(self.bu3,(self.bu3.get_width()*0.8,self.bu3.get_height()*0.7))
        self.bu = [self.bu1,self.bu2,self.bu3]
        self.changeimage = 0
        self.image = self.bu[self.changeimage]
        self.rect = self.image.get_rect()
        self.frame = 5
        self.vel_x = 0
        self.vel_y = 8

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.frame == 0:
            if self.changeimage < len(self.bu)-1:
                self.changeimage +=1
            self.image = self.bu[self.changeimage]
            self.frame = 5
        else : self.frame -=1