import pygame
import constants as c
from healthbar import HealthBar
from heart_icon import HeartIcon
from score import Score
from lives import Lives


class HUD(pygame.sprite.Sprite):
    def __init__(self,hp,num_lives):
        super(HUD,self).__init__()
        self.image = pygame.image.load('graphics/HUD3.png').convert_alpha()
        self.rect =self.image.get_rect()
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height
        self.vel_x = 0
        self.vel_y = 0

        self.health_bar = HealthBar(hp)
        self.health_bar.rect.x = 15
        self.health_bar.rect.y = c.DISPLAY_HEIGHT-self.health_bar.rect.height-18
        self.health_bar_groups = pygame.sprite.Group()
        self.health_bar_groups.add(self.health_bar)

        self.heart_icon = HeartIcon()
        self.lives = Lives(num_lives)
        self.lives.rect.x = 170
        self.lives.rect.y = c.DISPLAY_HEIGHT-40
        self.icons_group = pygame.sprite.Group()
        self.icons_group.add(self.heart_icon)
        self.icons_group.add(self.lives)

        self.score = Score()
        self.score_group = pygame.sprite.Group()
        self.score_group.add(self.score)


    def update(self):
        #self.health_bar_groups.update()
        self.score_group.update()
        self.icons_group.update()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y