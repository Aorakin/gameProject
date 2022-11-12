import pygame
import constants as c
from bullet import Bullet
from hud import HUD


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship,self).__init__()
        self.image = pygame.image.load('graphics/ship1.png').convert_alpha()
        # self.image = pygame.transform.scale(self.image,(self.image.get.width()*1.5,self.image.get.height()*1.5))
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH//2
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height-49
        self.bullets = pygame.sprite.Group()
        self.snd_shoot = pygame.mixer.Sound('sound/shootsound.mp3')
        self.hud = HUD()
        self.hud_group = pygame.sprite.Group()
        self.hud_group.add(self.hud)
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.keys = pygame.key.get_pressed()

    def update(self):
        self.bullets.update()
        self.hud_group.update()
        for bullet in self.bullets:
            if bullet.rect.y <=0:
                self.bullets.remove(bullet)
        self.rect.x +=self.vel_x
        if self.rect.x <=0:
            self.rect.x=0
        elif self.rect.x >=c.DISPLAY_WIDTH - self.rect.width:
            self.rect.x = c.DISPLAY_WIDTH - self.rect.width
        self.rect.y +=self.vel_y

    def shoot(self):
        self.snd_shoot.play()
        new_bullet = Bullet()
        new_bullet.rect.x = self.rect.x + (self.rect.width//2)-2
        new_bullet.rect.y = self.rect.y
        self.bullets.add(new_bullet)

 
