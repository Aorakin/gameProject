import pygame
import constants as c
import math

class Bullet2(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet2,self).__init__()
        self.width = 4
        self.height = self.width+3
        self.size = (self.width,self.height)
        self.image = pygame.Surface(self.size)
        self.color = (255,255,255)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.time =0
        self.changean = math.pi/90
        self.angle = math.pi*3/10
        self.vel_x = 0
        self.vel_y = 0
        self.radius = 8

    def update(self):
        self.time+=0.025
        self.vel_x = math.cos(self.angle)*self.radius
        self.vel_y = math.sin(self.angle)*self.radius
        # distx = self.vel_x*self.time
        # disty = (self.vel_y * self.time)+((-4.9*(self.time)**2)/2)
        self.rect.x += round(self.vel_x)
        self.rect.y += round(-self.vel_y)
        if self.angle>=math.pi*7/10 or self.angle <= 0:
            self.changean *= -1
        self.angle +=self.changean
        
            