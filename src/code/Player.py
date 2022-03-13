import pygame
# playerX = 370
# playerY = 480
class Player:

    def __init__(self):
        self.playerX = 370
        self.playerY = 480
        self.playerX_changer = 0
        self.playerY_changer = 0
        self.sprite = pygame.image.load('src//assets/img/space-invaders.png')
        self.screen = pygame.display.set_mode((800,600))
        self.name = ""
    
    def player(self,playerX,playerY):
        self.screen.blit(self.sprite,(playerX,playerY))


    def checkCorners(self,playerXX,playerYY):
        if playerXX <= 0:
            playerXX = 0
            # print("0check")
        elif playerYY <=0:
            playerYY = 0
        elif playerXX >= 736:
            playerXX = 736
        else:
            if playerYY >=536:
                playerYY = 536


    def colliderCheck(self):
        pass

    def timer(clock):
        pass
        # clock = pygame.time.Clock()
        # font = pygame.font.SysFont(None, 100)
        # counter = 10
        # text = font.render(str(counter), True, (0, 128, 0))
        # timer_event = pygame.USEREVENT+1
        # pygame.time.set_timer(timer_event, 1000)
        # run = True
        # while run:
        #     clock.tick(60)
        #     for event in pygame.event.get():
        #         if event.type == timer_event:
        #             counter -= 1
        #             text = font.render(str(counter), True, (0, 128, 0))
        #             if counter == 0:
        #                 pygame.time.set_timer(timer_event, 0)                

        #     screen.fill((255, 255, 255))
        #     text_rect = text.get_rect(center = screen.get_rect().center)
        #     screen.blit(text, text_rect)
        #     pygame.display.flip()


