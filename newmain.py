import pygame
import constants as c
from ship import Ship
from background import BG
from enemy_spawn import EnemySpawner
from particleSpawner import ParticleSpawner
from menu2 import mainmenu
import botton
from score import outputscore
from enemy import Enemy


pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
pygame.mixer.init()

pygame.display.set_caption('To The Galaxy')

#display setup
display = pygame.display.set_mode(c.DISPLAY_SIZE)
fps=60
clock = pygame.time.Clock()
Black = (0,0,0)

#Music setup
# pygame.mixer.music.load('sound/music1.ogg')
# pygame.mixer.music.set_volume(0.2)
# pygame.mixer.music.play(loops=True)



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
enemy = Enemy()
score=0


#menusetup
bg = pygame.image.load('graphics/mainmenubg_use.jpg')
start=[pygame.image.load('graphics/start4.png'),pygame.image.load('graphics/start3.png').convert_alpha()]
quit = [pygame.image.load('graphics/quit3.png'),pygame.image.load('graphics/quit4.png').convert_alpha()]
scoreboard = [pygame.image.load('graphics/scoreBoard2.png'),pygame.image.load('graphics/scoreBoard1.png').convert_alpha()]
button_start = botton.Button(180,220,start[0],start[1],1)
button_quit = botton.Button(180,380,quit[0],quit[1],1)
button_scoreboard = botton.Button(180,300,scoreboard[0],scoreboard[1],1)
game_start = False
menustate = 'main'

def draw_text(text ,size,col,x,y):
    font1 = pygame.font.Font('Font_game/Noted.ttf',size)
    text_sur = font1.render(text,True,col)
    text_rect = text_sur.get_rect(center=(x,y))
    display.blit(text_sur,text_rect)

def moveship(key):    
    if key[pygame.K_a] and player.rect.x>0:
        player.rect.x-=5
    if key[pygame.K_d] and player.rect.x<328:
        player.rect.x+=5
    if key[pygame.K_w] and player.rect.y>450:
        player.rect.y-=5
    if key[pygame.K_s] and player.rect.y<c.DISPLAY_HEIGHT-player.rect.height-49:
        player.rect.y+=5
gamestate = True

while gamestate:
    
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_a :
            #     player.vel_x = -player.speed
            # elif event.key == pygame.K_d:
            #     player.vel_x = +player.speed
            if event.key == pygame.K_SPACE:
                player.shoot()
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_a:
        #         player.vel_x = 0
        #     elif event.key == pygame.K_d:
        #         player.vel_x = 0


    display.blit(bg,(0,0))
    Keys = pygame.key.get_pressed()
    #check if game is start
    if game_start == False:
        if menustate == 'main':
            draw_text('To The Galaxy',40,'white',(c.DISPLAY_WIDTH//2),100)
            draw_text('To The Galaxy',40,'blue',(c.DISPLAY_WIDTH//2)+2,102)
            if (button_start.draw(display)):
                game_start = True 
            if (button_scoreboard.draw(display)):
                menustate = 'scoreboard'
            if button_quit.draw(display):
                gamestate = False
            
        #check other state
        if menustate == 'scoreboard':
            draw_text("score board",50,'black',180,250)
            if botton.Button.draw_text(botton.Button,'back',20,30,20,display):
                menustate = 'main'
        if menustate == 'pause':
            draw_text("pause",40,'black',180,80)
            if botton.Button.draw_text(botton.Button,'resume',40,180,250,display):
                game_start = True
            if botton.Button.draw_text(botton.Button,'Back To Mainmenu',40,180,330,display):
                menustate = 'main'
      
    #display menu
    else:
        
        if Keys[pygame.K_p]: 
            menustate= 'pause'
            game_start = False
        
        moveship(Keys)
        #Update all the objucts
        bg_group.update()
        sprite_group.update()
        enemy_spawner.update()
        particle_spawner.update()
    
        
        

        #Check colliision
        collided = pygame.sprite.groupcollide(player.bullets,enemy_spawner.enemy_group,True,False)
        for bullet,enemy in collided.items():
            enemy[0].get_hit()
            if not enemy[0].invincible:
                particle_spawner.spawn_particles((bullet.rect.x,bullet.rect.y))
           



        #Render the display
        display.fill(Black)
        bg_group.draw(display)
        sprite_group.draw(display)
        player.bullets.draw(display)
        enemy_spawner.enemy_group.draw(display)
        particle_spawner.particle_group.draw(display)
        #draw_text(f'SCORE: {enemy.score}',18,'white',280,20)
        player.hud_group.draw(display)
        player.hud.health_bar_groups.draw(display)
        
        
    clock.tick(fps)
    pygame.display.update()

pygame.quit()