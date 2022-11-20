import pygame
import constants as c
import sys
import random


class Item(pygame.sprite.Sprite):
    def __init__(self,x,y,itemtype,name):
        super(Item,self).__init__()
        self.ID = itemtype
        self.image = pygame.image.load(name).convert_alpha()
        #self.pos = vec(x,y)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = random.randrange(2,6)

    def update(self):
        self.rect.x  +=self.vel_x
        self.rect.y  += self.vel_y
        #print(self.ID)
       

    def rander(self,display):
        display.blit(self.image,self.pos)



#ID ->0 ->2way
#ID -> 1 -> hb
#ID -> 2 -> particle damage