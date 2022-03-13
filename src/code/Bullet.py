import pygame
import math

class Bullet:
    def __init__(self):
        self.bulletX = 370
        self.bulletY = 480
        self.bulletImg = pygame.image.load('src/assets/img/bulletImg.png')
        self.bulletX_changer = 0
        self.bulletY_changer = .7
        self.bullet_state = "ready"
        self.screen = pygame.display.set_mode((800,600))


    # def fire_bullet(self,bulletX,bulletY):
    #     # x = player.playerX
    #     # y = player.playerY
    #     # print("x-axis: ",x," y-axis: ", y)
    #     self.bullet_state = "fire"
    #     self.screen.blit(self.bulletImg, (bulletX + 16, bulletY + 20))
    #     print("x-axis: ",bulletX," y-axis: ", bulletY)

    def fire_bullet(self,x, y):
        self.bullet_state = "fire"
        self.screen.blit(self.bulletImg, (x + 16, y + 10))
        # print("x-axis: ",x," y-axis: ", y)



    # def bullet_stat(self):
    #     if self.bulletY <= 0:
    #         self.bulletY = 480
    #         self.bullet_state = "ready"

    #     if self.bullet_state == "fire":

    #         self.fire_bullet(self.bulletX,self.bulletY)
    #         self.bulletY -= self.bulletY_changer

    def isCollision(self,enemyX,enemyY,bulletX,bulletY):
        distance = math.sqrt((pow(enemyX - bulletX,2)) + (pow(enemyY - bulletY ,2)))
        if distance <= 27:
            return True
        else:
            return False