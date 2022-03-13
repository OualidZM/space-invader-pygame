import pygame
import random
from code.Bullet import Bullet

bullet = Bullet()
class Enemy:
    def __init__(self):
        self.number_of_enemies = 50
        # self.number_of_enemies = number_of_enemies
        self.enemayImg = []
        self.enemayX = []
        self.enemayY = []
        # normal change velocity
        self.enemayX_changer = []
        self.enemayY_changer = []
        self.playerX_changer_basic = 0
        self.playerX_changer_hard = 0
        # self.playerY_changer_hard = 0

        self.screen = pygame.display.set_mode((800,600))
        self.score_value = 0
        self.municion = 10
        self.difficulty = 0
        self.value_difficulty = ()




    def appendData(self):
        for i in range(self.number_of_enemies):
            self.enemayImg.append(pygame.image.load('src//assets/img/alien.png'))
            self.enemayX.append(random.randint(0,735))
            self.enemayY.append(random.randint(50,150))
            self.enemayX_changer.append(0.7)
            self.enemayY_changer.append(40)

    def enemy(self,x,y,i):
        self.screen.blit(self.enemayImg[i],(x,y))
    

    def respawn_enemy(self,enemayX,enemayY,bulletX,bulletY,i):
        collision = bullet.isCollision(enemayX[i],enemayY[i],bulletX,bulletY)
        print(collision)
        if collision:
            bulletY = 480
            bullet.bullet_state = "state"
            self.score_value += 1
            enemayX[i] = random.randint(0,735)
            enemayY[i] = random.randint(50,150)