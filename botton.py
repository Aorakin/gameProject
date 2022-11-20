from email.mime import image
from turtle import pos
import pygame

#botton class
class Button(pygame.sprite.Sprite):
    def __init__(self,x,y,image1,image2,scale):
        super(Button,self).__init__()
        self.buttonimg = image1
        self.buttonimg = pygame.transform.scale(self.buttonimg,(self.buttonimg.get_width()*scale,self.buttonimg.get_height()*scale))
        self.buttonimg2 = image2
        self.buttonimg2 = pygame.transform.scale(self.buttonimg2,(self.buttonimg2.get_width()*scale,self.buttonimg2.get_height()*scale))
        self.button = [self.buttonimg,self.buttonimg2]
        self.changeimg = 0
        self.image = self.button[self.changeimg]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.clicked = False
        
  
  

    def draw_text(self,text,size,X,Y,screen):
        mouse_pos = pygame.mouse.get_pos()
        font1 = pygame.font.Font('Font_game/Noted.ttf',size)
        text_sur = font1.render(text,True,'white')
        text_rect = text_sur.get_rect(center=(X,Y))
        if text_rect.collidepoint(mouse_pos) :
            text_sur = font1.render(text,True,'orange')
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return True
            if pygame.mouse.get_pressed()[0] == 0 :
                self.clicked = False
        screen.blit(text_sur,text_rect)

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) :
            self.changeimg = 1
            self.image = self.button[self.changeimg]
        else:   
            self.changeimg =0
            self.image = self.button[self.changeimg]
        print('draw')

    def checkclick(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) :
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return True
            if pygame.mouse.get_pressed()[0] == 0 :
                self.clicked = False
        
