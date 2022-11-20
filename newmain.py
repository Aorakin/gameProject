import pygame
import constants as c
from ship import Ship
from background import BG
from enemy_spawn import EnemySpawner
from particleSpawner import ParticleSpawner
from menu2 import mainmenu
import botton
from enemy_2 import Enemy2
from enemy import Enemy
from alert_box import AlertBox
from item import Item
import math
import json

#9-15 187 188 109 110
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption('To The Galaxy')

#display setup
display = pygame.display.set_mode(c.DISPLAY_SIZE) #, pygame.FULLSCREEN | pygame.HWACCEL)
fps=60
clock = pygame.time.Clock()
Black = (0,0,0)

# Music setup
pygame.mixer.music.load('sound/background.wav')
pygame.mixer.music.set_volume(0.2)




#object setup
bg = BG()
player = Ship()
bg_group = pygame.sprite.Group()
bg_group.add(bg)
sprite_group = pygame.sprite.Group()
sprite_group.add(player)
enemy_spawner = EnemySpawner()
particle_spawner = ParticleSpawner()
menu = mainmenu()
menu_group = pygame.sprite.Group()
menu_group.add(menu)
aler_box_group = pygame.sprite.Group()

button_group = pygame.sprite.Group()
Item = pygame.sprite.Group()
# enemy1 = Enemy()
enemy2 = Enemy2()
score=0 
speedstate = [5,10]
bulletstate = False
timetochange = pygame.time.get_ticks()
timetochange2 = pygame.time.get_ticks()
upship = False
count =1
upspeed = 6
haveboss = True


#menusetup
bg1 = pygame.image.load('graphics/mainmenubg_use.jpg')
start=[pygame.image.load('graphics/start4.png'),pygame.image.load('graphics/start3.png').convert_alpha()]
quit = [pygame.image.load('graphics/quit3.png'),pygame.image.load('graphics/quit4.png').convert_alpha()]
scoreboard = [pygame.image.load('graphics/scoreBoard2.png'),pygame.image.load('graphics/scoreBoard1.png').convert_alpha()]
backtomenu = [pygame.image.load('graphics/backtomenu1.png'),pygame.image.load('graphics/backtomenu2.png').convert_alpha()]
button_start = botton.Button(180,220,start[0],start[1],1)
button_quit = botton.Button(180,380,quit[0],quit[1],1)
button_scoreboard = botton.Button(180,300,scoreboard[0],scoreboard[1],1)
game_start = False
menustate = 'main'
#date
player_name = ''
data_score = {}
try:
    with open('score.json') as score_file:
        data_score = json.load(score_file)
except:
    pass


def draw_text(text ,size,col,x,y):
    font1 = pygame.font.Font('Font_game/Noted.ttf',size)
    text_sur = font1.render(text,True,col)
    text_rect = text_sur.get_rect(center=(x,y))
    display.blit(text_sur,text_rect)

def moveship(key,speed):    
    if key[pygame.K_a] and player.rect.x>0:
        player.rect.x-=speed
    if key[pygame.K_d] and player.rect.x<328:
        player.rect.x+=speed
    if key[pygame.K_w] and player.rect.y>c.DISPLAY_HEIGHT//2:
        player.rect.y-=speed
    if key[pygame.K_s] and player.rect.y<c.DISPLAY_HEIGHT-player.rect.height-49:
        player.rect.y+=speed
gamestate = True

def gameover():
        enemy_spawner.clear_enemies()
        alert_box = AlertBox('GAME OVER',-180,40)
        draw_score = AlertBox(f'your score : {score}',50,32)
        enter_yourname = AlertBox('Enter Your Name',-100,32)
        draw_back = AlertBox('back to menu',120,28)
        aler_box_group.add(alert_box)
        aler_box_group.add(draw_score)
        aler_box_group.add(draw_back)
        aler_box_group.add(enter_yourname)
        
def text_input(score):
    player_name = ''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                player_name = player_name[:-1]
            elif event.key == pygame.K_RETURN and len(player_name) >= 1:
                data_score[player_name] = score
                with open('score.json', 'w') as score_file:
                    json.dump(data_score,score_file)
            else:
                player_name += event.unicode
    
def board():
    with open('score.json', 'r') as score_file:
        data_score = json.load(score_file)
    offset = 0
    count = 0
    sorted_name = sorted(data_score.items(), key=lambda x:x[1], reverse=True)
    sorted_dict = dict(sorted_name)
    name = list(sorted_dict.keys())
    for key in name:
            if count <= 4:
                name = AlertBox(key,20,28)
                aler_box_group.add(name)
                score_surf =AlertBox(str(int(sorted_dict[key])),100+offset,28)
                aler_box_group.add(score_surf)
                offset += 100
                count += 1

    


while gamestate:
    
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT  :
            # with open('score_data.txt','w') as  score_file:
            #     json.dump(data_score,score_file)
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bulletstate:
                    player.shoot2way()
                    if upship :
                        player.shoot3way()
                else: player.shoot()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if not player.is_alive:
                
                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                    # print(Yourname.message)
                    # for i in aler_box_group :
                    #     aler_box_group.remove(i)
                    # aler_box_group.message[:-1]
                elif event.key == pygame.K_RETURN and len(player_name) >= 1:
                    data_score[player_name] = score
                    print('enter')
                    with open('score.json', 'w') as score_file:
                        json.dump(data_score,score_file)
                
                else:
                    player_name += event.unicode
                        
            



    display.blit(bg1,(0,0))
    Keys = pygame.key.get_pressed()
    #check if game is start
    if game_start == False:
        if menustate == 'main':
            for i in button_group:
                button_group.remove(i)
            button_group.add(button_start)
            button_group.add(button_scoreboard)
            button_group.add(button_quit)
            button_start.draw()
            button_scoreboard.draw()
            button_quit.draw()
            bg.reset_bg()
            draw_text('To The Galaxy',40,'white',(c.DISPLAY_WIDTH//2),100)
            draw_text('To The Galaxy',40,'blue',(c.DISPLAY_WIDTH//2)+2,102)
            if (button_start.checkclick()):
                game_start = True
                pygame.mixer.music.play(-1)
                starttime = pygame.time.get_ticks() 
                score = 0
            if (button_scoreboard.checkclick()):
                menustate = 'scoreboard'
            if button_quit.checkclick():
                gamestate = False
            
        #check other state
        if menustate == 'scoreboard':
            for i in button_group:
                button_group.remove(i)
            pygame.draw.rect(display,'orange',[75,140,200,40])
            pygame.draw.rect(display,'white',[75,120,200,40])
            draw_text('ranking',28,'black',170,135)
            # draw_text("score board",50,'black',180,250)
            with open('score.json', 'r') as score_file:
                data_score = json.load(score_file)
            offset = 0
            count = 0
            sorted_name = sorted(data_score.items(), key=lambda x:x[1], reverse=True)
            sorted_dict = dict(sorted_name)
            name = list(sorted_dict.keys())
            pygame.draw.rect(display,'black',[75,165,200,320])
            for key in name:
                    if count <= 4:
                        # name = AlertBox(key,20,28)
                        # aler_box_group.add(name)
                        # score_surf =AlertBox(str(int(sorted_dict[key])),100+offset,28)
                        # aler_box_group.add(score_surf)
                        draw_text(key,28,'white',125,180+offset)
                        draw_text(str(int(sorted_dict[key])),28,'white',220,180+offset)
                        offset += 60
                        count += 1
            if botton.Button.draw_text(botton.Button,'back',20,30,20,display):
                menustate = 'main'
        if menustate == 'pause':
            for i in button_group:
                button_group.remove(i)
            draw_text("pause",40,'black',180,80)
            if botton.Button.draw_text(botton.Button,'resume',40,180,250,display):
                game_start = True
            if botton.Button.draw_text(botton.Button,'Back To Mainmenu',40,180,330,display):
                menustate = 'main'
        if menustate == 'gameover':
            draw_text("game over",40,'white',180,150)
            if botton.Button.draw_text(botton.Button,'Back To Mainmenu',40,180,330,display):
                menustate = 'main'
        button_group.update()
        button_group.draw(display)
    #display menu
    else:
        time_since_start = (pygame.time.get_ticks()-starttime)//1000
        if Keys[pygame.K_p] and player.is_alive: 
            menustate= 'pause'
            game_start = False
            
        if upship:
            moveship(Keys,speedstate[1])
            for bu in player.bullets:
                bu.vel_y = -12
        else:
            moveship(Keys,speedstate[0])
            for bu in player.bullets:
                bu.vel_y = -6
            

        #Update all the objucts
        bg_group.update()
        sprite_group.update()
        enemy_spawner.update()
        particle_spawner.update()
        aler_box_group.update()
    
        

        #Check colliision
        for bullet in player.bullets:
            for enemy in enemy_spawner.enemy_group:
                if not enemy.invincible:
                    if bullet.rect.colliderect(enemy.rect) and bullet.rect.top-enemy.rect.bottom<5:
                        enemy.get_hit()
                        if enemy.destroyed:
                            player.hud.score.update_score(enemy.score_value)
                            score += enemy.score_value
                        if not enemy.invincible:
                            particle_spawner.spawn_particles((bullet.rect.x,bullet.rect.y)) 
                        player.bullets.remove(bullet)
                                  
        collided = pygame.sprite.groupcollide(sprite_group,enemy_spawner.enemy_group,False,False)
        for player,enemy in collided.items():
            if not enemy[0].invincible and not player.invincible:
                player.get_hit()
                enemy[0].hp = 0
                enemy[0].get_hit()
        for enemy in enemy_spawner.enemy_group:
            collided = pygame.sprite.groupcollide(sprite_group,enemy.bullets,False,True)
            for player,bullet in collided.items():
                if not player.invincible:
                    player.get_hit()

        collided = pygame.sprite.groupcollide(sprite_group,enemy_spawner.item,False,True)
        for player,check in collided.items():
            if check[0].ID == 1:
                player.increase_hp()
            if check[0].ID == 0 :
                bulletstate = True
                timetochange = pygame.time.get_ticks()
            if check[0].ID == 2:
                upship = True
                timetochange2 = pygame.time.get_ticks()

        for enemy in enemy_spawner.enemy_group:
            collided = pygame.sprite.groupcollide(sprite_group,enemy.item,False,True)
            for player,check in collided.items():
                enemy_spawner.enemy_group.remove(enemy)
                if check[0].ID == 1:
                    player.increase_hp()
                if check[0].ID == 0 :
                    bulletstate = True
                    timetochange = pygame.time.get_ticks()
                if check[0].ID == 2:
                    upship = True
                    timetochange2 = pygame.time.get_ticks()

        #game over
        if not player.is_alive:
            gameover()
            draw_back = AlertBox('back to menu',120,28)
            button_group.add(draw_back)
            if draw_back.check():
                game_start = False
                menustate = 'main'
            # Yourname = AlertBox(player_name,20,28)
            # aler_box_group.add(Yourname)
            font1 = pygame.font.Font('Font_game/Noted.ttf',28)
            text_sur = font1.render(player_name,False,'white')
            text_rect = text_sur.get_rect(center=(180,320))
 

        
        if pygame.time.get_ticks() - timetochange >=10000:
            bulletstate = False
        if pygame.time.get_ticks() - timetochange2 >=10000:
            upship = False
        if time_since_start >= 180 and haveboss :
            for i in range(3):
                player.increase_hp()

            enemy_spawner.bossstate = True
            haveboss = False
                
        if time_since_start == 45*count:
                print('crazy')
                enemy_spawner.crazy_spawn(count)
                count+=1


        #Render the display
        display.fill(Black)
        bg_group.draw(display)
        sprite_group.draw(display)
        player.bullets.draw(display)
        enemy_spawner.enemy_group.draw(display)
        particle_spawner.particle_group.draw(display)
        for enemy in enemy_spawner.enemy_group:
            enemy.bullets.draw(display)
        enemy_spawner.item.draw(display)
        for item in enemy_spawner.enemy_group:
            item.item.draw (display)
        #draw_text(f'SCORE: {enemy.score}',18,'white',280,20)
        player.hud_group.draw(display)
        player.hud.health_bar_groups.draw(display)
        player.hud.score_group.draw(display)
        player.hud.icons_group.draw(display)
        aler_box_group.draw(display)
        if not player.is_alive:
            font1 = pygame.font.Font('Font_game/Noted.ttf',28)
            text_sur = font1.render(player_name,False,'white')
            text_rect = text_sur.get_rect(center=(180,320))
            display.blit(text_sur,text_rect)
        

            
           
    
        
        
        
    clock.tick(fps)
    pygame.display.update()

pygame.quit()
