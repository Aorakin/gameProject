import pygame
import constants as c

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
        self.speed = [6,12]
        self.vel_x = 0
        self.vel_y = -self.speed[0]

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y