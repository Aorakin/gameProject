import pygame
import constants as c

class Bulleten(pygame.sprite.Sprite):
    def __init__(self):
        super(Bulleten,self).__init__()
        self.width = 4
        self.height = self.width+3
        self.size = (self.width,self.height)
        self.image = pygame.Surface(self.size)
        self.color = ('yellow')
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 10

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        #เพิ่งเพิ่มไม่รู้บัคมั้ย
        if self.rect.x <=0 or self.rect.x>=c.DISPLAY_WIDTH:
            self.vel_x *=-1