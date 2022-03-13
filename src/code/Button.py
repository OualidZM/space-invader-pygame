import pygame

class Button:
    def __init__(self,color,x,y,buttonW,buttonH,text=""):
        self.color = color
        self.x = x
        self.y = y
        self.buttonW = buttonW
        self.buttonH = buttonH
        self.text = text
        self.screen = pygame.display.set_mode((800,600))


    def draw(self,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(self.screen, outline, (self.x-2,self.y-2,self.buttonW+4,self.buttonH+4),0)
            
        pygame.draw.rect(self.screen, self.color, (self.x,self.y,self.buttonW,self.buttonH),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            self.screen.blit(text, (self.x + (self.buttonW/2 - text.get_width()/2), self.y + (self.buttonH/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.buttonW:
            if pos[1] > self.y and pos[1] < self.y + self.buttonH:
                return True
            
        return False