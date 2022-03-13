import pygame
import pygame_menu
import random
import math
from pygame import mixer
from code.Player import Player
from code.Enemy import Enemy
from code.Bullet import Bullet
from code.Button import Button
import sys

player = Player()
enemy = Enemy()
bullet = Bullet()
button = Button((0,255,0),250,350,250,100,'Restart')
# inizialice game
pygame.init()
mixer.init()
#creatind screen
screen = pygame.display.set_mode((800,600))

# Screen title
pygame.display.set_caption("Space invadors")

#Space and icons
icon = pygame.image.load('src//assets/img/spaceship_icon.png')
pygame.display.set_icon(icon)

# background
backgroundBg = pygame.image.load('src//assets/img/space-bg.jpg')

# background sound
mixer.music.load('src/assets/sounds/space_mus.flac')
mixer.music.play(-1)


# Enemy
enemy.appendData()

# Bullet
bulletX = bullet.bulletX
bulletY = bullet.bulletY
bulletX_changer = 0
bulletY_changer = .7
bullet_state = "ready"

# Player

playerX = 370
playerY = 480


#score text
score_value = enemy.score_value
font = pygame.font.Font('freesansbold.ttf',32)
text_score_X = 15
text_score_Y = 40

# Munition text
text_municion_X = 570
text_municion_Y = 10

# Reload text
text_reload_X = 450
text_reload_Y = 10
font_count_down = pygame.font.Font('freesansbold.ttf',32)

# name text

text_name_X = 15
text_name_Y = 10
font_name_value = pygame.font.Font('freesansbold.ttf',32)


# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf',64)

# display text

def show_score(x,y):
    score = font.render("Score: " + str(enemy.score_value),True,(255,255,255))
    screen.blit(score,(x,y))

# call show_name function
def show_name_call(name):
    player.name = name
    show_name(name,text_name_X,text_name_Y)

# show_name, to display name
def show_name(namePlayer,x,y):
    if namePlayer == "":
        namePlayer = "Guest"
        name = font_name_value.render(namePlayer,True,(255,255,255))
        screen.blit(name,(x,y))
    else:
        name = font_name_value.render(namePlayer,True,(255,255,255))
        screen.blit(name,(x,y))

# show actual munition
def show_municion(x,y):
    municion = font.render("Munition: " + str(enemy.municion),True,(255,255,255))
    screen.blit(municion,(x,y))

# show count down when player doesn't have munition
def count_down(x,y,counddown):
    reloading_s = font_count_down.render("Reloading: " + str(counddown),True,(255,255,255))
    screen.blit(reloading_s,(x,y))
# Collision

# game over text
def game_over_text():
    lost_text = over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(lost_text,(200,250))

# collision detection
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((pow(enemyX - bulletX,2)) + (pow(enemyY -bulletY ,2)))
    
    if distance <= 27:
        return True
    else:
        return False

# set difficulty
def set_difficulty(value, difficulty):
    enemy.value_difficulty  = value
    enemy.difficulty = difficulty
    enemy.number_of_enemies = 15
    if enemy.difficulty == 1 or enemy.difficulty == 0:
        enemy.playerX_changer_basic = .7
        enemy.municion = 15
        
        return 1

    elif enemy.difficulty == 2:
        enemy.playerX_changer_hard = 2
        enemy.number_of_enemies = 35
        return 2

# Run game
def run_game():
    start_the_game(playerX,playerY,bulletX,bulletY)

    
# Game
def start_the_game(playerX,playerY,bulletX,bulletY):
    # Do the job here !
    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(backgroundBg,(0,0))
        show_score(text_score_X,text_score_Y)
        show_municion(text_municion_X,text_municion_Y)
        show_name(player.name,text_name_X,text_name_Y)
        if enemy.municion == 0:
            counddown = []
            for i in range(5):
                # print("reloading")
                counddown.append(1)
                # print(counddown[i])
                count_down(text_reload_X,text_reload_Y,counddown[i])
                
            
            enemy.municion +=15
        else:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                
                key = pygame.key.get_pressed()
                pos = pygame.mouse.get_pos()


                if key[pygame.K_RIGHT]:
                    player.playerX_changer += 10

                if key[pygame.K_LEFT]:
                    player.playerX_changer += -10

                if key[pygame.K_UP]:
                    player.playerY_changer += -10

                if key[pygame.K_DOWN]:
                    player.playerY_changer += 10
                if key[pygame.K_SPACE]:
                    if enemy.municion != 0:
                        bulletX = playerX
                        bulletY = playerY
                        # print(bulletX)
                        bullet.fire_bullet(bulletX,bulletY)
                        enemy.municion -= 1
                        explosion_sound = mixer.Sound('src/assets/sounds/bullet_sound.wav')
                        explosion_sound.play()
                    else:
                        # player.timer()
                        pass
                            # pygame.time.delay(1000)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button.isOver(pos):
                        print("clicking")
                        enemy.score_value = 0
                        enemy.municion = 15
                        playerX = 370
                        playerY = 480
                        for i in range(enemy.number_of_enemies):
                            enemy.enemayY[i] = random.randint(50,150)
                    else:
                        print("no Clickig")

                    

                    # print("x-axis: ",bulletX," y-axis: ", bulletY)
                
                    # bullet.fire_bullet()
                    # bullet_state = "fire"
                    # bulletX = player.playerX
                    # bulletY = player.playerY

                    # fire_bullet(bulletX,bulletY) 

                    # mixer.music.load('./assets/sounds/bullet_sound.wav')
                    # explosion_sound = mixer.Sound('src/assets/sounds/bullet_sound.wav')
                    # explosion_sound.play()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player.playerX_changer = 0
                        player.playerY_changer = 0
                    
                    
        # Player check corners
        playerX += player.playerX_changer
        playerY += player.playerY_changer    

        player.checkCorners(playerX,playerY)
        

        # Enemy check corners
        for i in  range(enemy.number_of_enemies):
            # Game Over

            if enemy.enemayY[i] > playerY:
                for j in range(enemy.number_of_enemies):
                    enemy.enemayY[j] = 2000
                playerX = 2000
                game_over_text()
                button.draw()
                

                break
            set_difficulty(enemy.value_difficulty,enemy.difficulty)
            # # movement enemy x-axis
            if enemy.difficulty == 1 or enemy.difficulty == 0:
                enemy.enemayX[i] += enemy.enemayX_changer[i]
                if enemy.enemayX[i] <= 0:
                
                    enemy.enemayX_changer[i] = enemy.playerX_changer_basic
                    enemy.enemayY[i] += enemy.enemayY_changer[i]
                elif enemy.enemayX[i] >= 736:
                    enemy.enemayY[i] += enemy.enemayY_changer[i]
                    enemy.enemayX_changer[i] = -enemy.playerX_changer_basic

            elif enemy.difficulty == 2:
                enemy.enemayX[i] += enemy.enemayX_changer[i]
                if enemy.enemayX[i] <= 0:
                
                    enemy.enemayX_changer[i] = enemy.playerX_changer_hard
                    enemy.enemayY[i] += enemy.enemayY_changer[i]
                elif enemy.enemayX[i] >= 736:
                    enemy.enemayY[i] += enemy.enemayY_changer[i]
                    enemy.enemayX_changer[i] = -enemy.playerX_changer_hard

            # basic
            


            collision = isCollision(enemy.enemayX[i],enemy.enemayY[i],bulletX,bulletY)
            if collision:
                bulletY = 480
                bullet.bullet_state = "ready"
                enemy.score_value += 1
                enemy.enemayX[i] = random.randint(0,735)
                enemy.enemayY[i] = random.randint(50,150)
                enemy_sound = mixer.Sound('src/assets/sounds/enemy_death.wav')
                enemy_sound.play()
                # print(enemy.score_value)
            enemy.enemy(enemy.enemayX[i],enemy.enemayY[i],i)

            # bullet movement 
            if bulletY <= 0:
                bulletY = 480
                # print(bulletY)
                bullet.bullet_state = "ready"

            if bullet.bullet_state == "fire":
                bullet.fire_bullet(bulletX,bulletY)
                bulletY -= bullet.bulletY_changer
            # print("x-axis: ",bulletX," y-axis: ", bulletY)

        # Collision
        player.player(playerX,playerY)
        pygame.display.update()


# creation of menu
menu = pygame_menu.Menu('Welcome', 400, 300,theme=pygame_menu.themes.THEME_BLUE)

# adding input name
menu.add.text_input('Name :', default='',onchange=show_name_call)

# adding input name
menu.add.selector('Difficulty :', [('Easy', 1), ('Hard', 2)], onchange=set_difficulty)

menu.add.button('Play', run_game)

menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)


