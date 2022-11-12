import pygame
import constants as c

class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        super(HealthBar,self).__init__()
        self.image = pygame.image.load('graphics/Health100.png').convert()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*0.25,self.image.get_height()*0.25))
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0
      

    def update(self):
        self.rect.x = self.vel_x
        self.rect.y = self.vel_y