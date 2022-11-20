import pygame
import constants as c
import random

class Planet(pygame.sprite.Sprite):
    def __init__(self):
        super(Planet,self).__init__()
        self.planet_01 = pygame.image.load('graphics/planet1.png').convert_alpha()
        self.planet_02 = pygame.image.load('graphics/planet2.png').convert_alpha()
        self.planet_03 = pygame.image.load('graphics/planet3.png').convert_alpha()
        self.planet_04 = pygame.image.load('graphics/planet4.png').convert_alpha()
        self.planet_05 = pygame.image.load('graphics/planet5.png').convert_alpha()
        self.planet_06 = pygame.image.load('graphics/planet6.png').convert_alpha()
        self.planet_07 = pygame.image.load('graphics/planet7.png').convert_alpha()
        self.planet_08 = pygame.image.load('graphics/planet8.png').convert_alpha()
        self.planet_09 = pygame.image.load('graphics/planet9.png').convert_alpha()
        self.img_planets = [self.planet_01,
                            self.planet_02,
                            self.planet_03,
                            self.planet_04,
                            self.planet_05,
                            self.planet_06,
                            self.planet_07,
                            self.planet_08,
                            self.planet_09]

        self.num_planet = len(self.img_planets)
        self.img_index = random.randrange(0,self.num_planet-1)
        self.image = self.img_planets[self.img_index]
        self.scale_value = random.uniform(1.25,1.75)
        self.image = pygame.transform.scale(self.image,(int(self.image.get_width()*self.scale_value),int(self.image.get_height()*self.scale_value)))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,c.DISPLAY_WIDTH-self.rect.width)
        self.rect.y = 0-self.rect.height  
        self.pos_x = random.randrange(0,c.DISPLAY_WIDTH-self.rect.width)
        self.pos_y = 0-self.rect.height
        self.vel_x = 0.0
        self.vel_y = random.uniform(0.2,2.0)

    def update(self):
        self.pos_x +=self.vel_x
        self.pos_y +=self.vel_y 
        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)

