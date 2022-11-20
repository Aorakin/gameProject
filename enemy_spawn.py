import pygame
from enemy import Enemy
from enemy_2 import Enemy2
from enemy_3 import Enemy3
from enemy_4 import Enemy4
from item import Item
import constants as c
import random

class EnemySpawner :
    def __init__(self):
        self.enemy_group = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30,120)
        self.timer2_max = 720
        self.timer2 = self.timer2_max
        self.current_time = pygame.time.get_ticks()
        self.current_time1 = pygame.time.get_ticks()
        self.current_time2 = pygame.time.get_ticks()
        self.timeen3 = pygame.time.get_ticks()
        self.count = 1
        self.count2 = 1
        self.crazy = 30
        self.checkspawn = True
        self.bossstate =False
        self.clear = True
        self.destroy = False
        self.item = pygame.sprite.Group()
        self.differ = 0.5
        self.speed = 7
        

    def update(self):
        self.item.update()
        #print(pygame.time.get_ticks()//1000)
        self.enemy_group.update()
        for enemy in self.enemy_group:
            if enemy.rect.y>=c.DISPLAY_HEIGHT:
                self.enemy_group.remove(enemy)
        if self.bossstate:
            self.fightboss()
            self.differ=18
            self.checkbossdestroy()
            if pygame.time.get_ticks() - self.current_time1 >=8000:
                self.genitem()
                print('item')
                self.current_time1 = pygame.time.get_ticks()     
        else:
            self.any_enemy()
            self.speedup()
            
        

        
        
    def cooldown(self,sec):
        curtime = pygame.time.get_ticks()
        if pygame.time.get_ticks() - curtime >= sec:
            return True
        else : False
    def any_enemy(self):
        if self.spawn_timer <= 0:
                self.spawn_enemy_1()
                self.spawn_timer = random.randrange(50,120)-self.differ
        else:self.spawn_timer-=1
        if (pygame.time.get_ticks() - self.current_time2)//1000 >=5:
            print('spawn')
            self.spawn_enemy_2()
            if self.differ<30:
                self.differ+=0.5
            if self.speed<=12:
                self.speed +=0.05
            print(self.speed)
            self.current_time2= pygame.time.get_ticks()
        if self.timer2 == 0:
            self.spawn_enemy_3()
            self.count2 +=1
            self.timer2 = self.timer2_max
        else:self.timer2-=1

    def crazy_spawn(self,count):
        for i in range(1,(self.count*5)):
            self.spawn_enemy_1()
            self.spawn_enemy_2()
            if i%3 ==0:
                self.spawn_enemy_3()
            count+=1

    def fightboss(self):
        if  self.clear:
                self.clear = False
                self.clear_enemies()
        if  pygame.time.get_ticks() >3000:
            #self.current_time2 = pygame.time.get_ticks()
            if self.checkspawn:
                self.checkspawn = False
                self.spawn_boss1()

    def spawn_enemy_1(self):
            new_enemy = Enemy()
            self.enemy_group.add(new_enemy)
    def spawn_enemy_2(self):
            new_enemy = Enemy2()
            self.enemy_group.add(new_enemy)

    def spawn_enemy_3(self):
        new_enemy = Enemy3()
        self.enemy_group.add(new_enemy)

    def spawn_boss1(self):
        print('spawn')
        new_enemy = Enemy4()
        self.enemy_group.add(new_enemy)

    def clear_enemies(self):
        for enemy in self.enemy_group:
            enemy.kill()
    def checkbossdestroy(self):
        for boss in self.enemy_group:
            if boss.destroyed:
                self.bossstate = False

    def speedup (self):
        for speed in self.enemy_group:
            speed.vel_y = self.speed

    def genitem(self):
        random_change = random.randrange(1,50)
        x = random.randrange(0,c.DISPLAY_WIDTH-2)
        y = 0
        if random_change >=1 and random_change<=15:
            item = Item(x,y,0,'graphics/item1.png')
            self.item.add(item)
        elif random_change>20 and random_change <=40:
            item = Item(x,y,1,'graphics/item2.png')
            self.item.add(item)
        elif random_change>40 and random_change <=60:
            item = Item(x,y,2,'graphics/item3.png')
            self.item.add(item)  