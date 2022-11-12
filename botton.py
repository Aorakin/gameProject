from email.mime import image
from turtle import pos
import pygame

#botton class
class Button():
    def __init__(self,x,y,image1,image2,scale):
        width1 = image1.get_width()
        height1 = image1.get_height()
        self.image1 = pygame.transform.scale(image1,(int(width1*scale),int(height1*scale)))
        width2 = image2.get_width()
        height2 = image2.get_height()
        self.image2 = pygame.transform.scale(image2,(int(width2*scale),int(height2*scale)))
        self.rect = self.image1.get_rect()
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

    def draw(self,surface):
        action = False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) :
            surface.blit(self.image2,self.rect)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            
            if pygame.mouse.get_pressed()[0] == 0 :
                self.clicked = False
        else:   surface.blit(self.image1,self.rect)
      
    

        return action