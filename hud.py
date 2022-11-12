import pygame
import constants as c
from healthbar import HealthBar

class HUD(pygame.sprite.Sprite):
    def __init__(self):
        super(HUD,self).__init__()
        self.image = pygame.image.load('graphics/HUD3.png').convert_alpha()
        self.rect =self.image.get_rect()
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height
        self.vel_x = 0
        self.vel_y = 0
        self.health_bar = HealthBar()
        self.health_bar.rect.x = 15
        self.health_bar.rect.y = c.DISPLAY_HEIGHT-self.health_bar.rect.height-18
        self.health_bar_groups = pygame.sprite.Group()
        self.health_bar_groups.add(self.health_bar)


    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y