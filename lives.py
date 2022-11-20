import pygame
import constants as c

class Lives(pygame.sprite.Sprite):
    def __init__(self,numlives):
        super(Lives,self).__init__()
        self.num_lives = numlives
        self.width = 65
        self.height = 37
        self.size = (self.width,self.height)
        self.image = pygame.Surface(self.size)
        self.image.set_colorkey((0,0,0))
        self.ship_image = pygame.image.load('graphics/ship1.png').convert_alpha()
        self.ship_image = pygame.transform.scale(self.ship_image,(self.ship_image.get_width()*0.7,
                                                                    self.ship_image.get_height()*0.7))
        self.image.blit(self.ship_image,(0,0))
        self.font_size = 24
        self.fontcolor = ('white')
        self.font = pygame.font.Font(None,self.font_size)
        self.lives_counter = self.font.render(f'x{self.num_lives}',False,self.fontcolor,False)
        self.image.blit(self.lives_counter,(35,10))
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0


    def update(self):
        pass
    

    def decrement_life(self):
        self.num_lives -=1
        if self.num_lives < 0 :
            self.num_lives = 0
            print('game over')
            return True
        else : pass
        self.image = pygame.Surface(self.size)
        self.image.set_colorkey((0,0,0))
        self.image.blit(self.ship_image,(0,0))
        self.lives_counter = self.font.render(f'x{self.num_lives}',False,self.fontcolor,False)
        self.image.blit(self.lives_counter,(35,10))