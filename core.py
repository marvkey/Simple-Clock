import pygame
import pygame.freetype 
pygame.init()
GAME_FONT = pygame.freetype.Font("assets/fonts/OpenSans-Bold.ttf", 15)
allButton =[]
class Button:
    height=0
    width=0
    x=0
    y=0
    colour=(200,200,200,255)
    text=""
    textcolor=(255,255,255,255)
    shape="rect"
    def __init__(self,x,y,height,width,text=""):
        self.x = x
        self.y = y
        self.height = height
        self.width = width  
        self.text = text
        allButton.append(self)  
    def onClick(self,event):
        return self.buttonclicked

    def IsButtonHovered(self):
        mouseX, mouseY = pygame.mouse.get_pos()
       # print(mouseX,mouseY)
        
        if ( (self.x+self.width) >= mouseX and self.x<= mouseX) and ( (self.y+self.height) >= mouseY and self.y<= mouseY):
            return True
        return False
    
    def Render(self,window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.height))
      
        GAME_FONT.render_to(window, (self.x+self.width/2, self.y+self.height/2), self.text, self.textcolor)


    def IsPressed(self):
        left, middle, right = pygame.mouse.get_pressed()
        if self.IsButtonHovered()==True and left:
            return True
        return False

    