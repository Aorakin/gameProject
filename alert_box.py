import pygame
import constants as c

class AlertBox(pygame.sprite.Sprite):
    def __init__(self,message,y,size):
        super(AlertBox,self).__init__()
        self.font = pygame.font.Font(None,size)
        self.color = 'white'
        self.message = message
        self.image = self.font.render(self.message,0,self.color)
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH //2-self.rect.width//2
        self.rect.y = c.DISPLAY_HEIGHT//2 +y
        self.vel_x = 0 
        self.vel_y = 0
        self.clicked = False

    def check(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) :
            self.color = 'yellow'
            self.image = self.font.render(self.message,0,self.color)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return True
            if pygame.mouse.get_pressed()[0] == 0 :
                self.clicked = False
        else : self.color = 'white'
        self.image = self.font.render(self.message,0,self.color)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y +=self.vel_y