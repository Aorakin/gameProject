import pygame
import constants as c


class HeartIcon(pygame.sprite.Sprite):
    def __init__(self):
        super(HeartIcon,self).__init__()
        self.img_heart1  =pygame.image.load('graphics/heart1.png').convert_alpha()
        self.img_heart2  =pygame.image.load('graphics/heart2.png').convert_alpha()
        self.img_heart3 =pygame.image.load('graphics/heart3.png').convert_alpha()
        self.img_heart4  =pygame.image.load('graphics/heart4.png').convert_alpha()
        self.img_heart5  =pygame.image.load('graphics/heart5.png').convert_alpha()
        self.img_heart6  =pygame.image.load('graphics/heart6.png').convert_alpha()
        self.anime_list = [self.img_heart1,
                        self.img_heart2,
                        self.img_heart3,
                        self.img_heart4,
                        self.img_heart5,
                        self.img_heart6]

        self.anime_index = 0
        self.max_index = len(self.anime_list)-1
        self.max_frame_duration = 6
        self.frame_duration = self.max_frame_duration
        self.image = self.anime_list[self.anime_index]
        self.rect = self.image.get_rect()
        self.rect.x =20
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height -45


    
    def update(self):
        if self.frame_duration == 0:
            self.anime_index +=1
            if self.anime_index > self.max_index:
                self.anime_index =0
            self.image = self.anime_list[self.anime_index]
            self.image = pygame.transform.scale(self.image,(self.image.get_width()*1.5,self.image.get_height()*1.5))
            self.frame_duration = self.max_frame_duration
        self.frame_duration -=1
            
