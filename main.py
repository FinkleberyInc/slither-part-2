#slither game
import pygame
import random
import math
pygame.init()
pygame.display.set_caption("slither")
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
doExit = False
#P variables
xPos = 200
yPos = 200
Vx = 1
Vy = 1

#start class pellet
class pellet:
    def __init__(self, xpos, ypos, red, green, blue, radius):
        self.xpos = xpos
        self.ypos = ypos
        self.red = red
        self.green = green
        self.blue = blue
        self.radius = radius
    def draw(self):
        pygame.draw.circle(screen, (self.red, self.green, self.blue), (self.xpos, self.ypos), self.radius)
    def collide(self,x,y):
        if math.sqrt((x-self.xpos)*(x-self.xpos)+(y-self.ypos)*(y-self.ypos)) < self.radius + 6:
            self.xpos = random.randrange(0,400)
            self.ypos = random.randrange(0,400)
            self.red = random.randrange(0,255)
            self.blue = random.randrange(0,255)
            self.green = random.randrange(0,255)
            self.radius = random.randrange(0,30)
            return True

pelletBag = list()#creates a list data strructure
tail = list()
for i in range (100):
    pelletBag.append(pellet(random.randrange(0,400),random.randrange(0,400),random.randrange(0,255),random.randrange(0,255),random.randrange(0,255),random.randrange(0,30)))   
#end class pellet
    #class tailsag
class TailSag:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
    def update(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.circle(screen,(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), (self.xpos, self.ypos), 12)                
oldX=200
oldY=200
counter = 0
#gameloop
while not doExit:
#event/input
    #clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
        else:
            doExit = False
    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
        if mousePos[0]>xPos:
            Vx = 1
        else:
            Vx = -1
        if mousePos[1]>yPos:
            Vy = 1
        else:
            Vy = -1
            
    counter + 1 #update counter
    if counter == 20: #create a delay so the segments follow behind
        counter = 0 #reset counter every 20 ticks
    oldX = xPos #hold onto old players position from 20 ticks ago
    oldY = yPos
    
    if (len(tail)>2): # don't push numbers if they are no nodes yet
        for i in range(len(tail)):#loop for each slot in list
            #start in LAST position, push the *second to last* into it, reoeat till at beginning
            tail[len(tail)-i-1].xpos = tail[len(tail)-i-2].xpos
            tail[len(tail)-i-1].ypos = tail[len(tail)-i-2].ypos
    if(len(tail)>0): #If you have at least one segment; push old head position into that
        tail[0].update(oldX,oldY) #push head position into first position of list

#physics
if xPos<0 or xPos+12>400 or yPos<0 or yPos+12>400:
    doExit = True
        
#update circle position
    xPos += Vx
    yPos += Vy
#render to screen
    screen.fill((255,255,255))
    for i in range (10):
        if pelletBag[i].collide(xPos,yPos)==True:
           tail.append(TailSag(oldX,oldY))
    for i in range(len(tail)):
        tail[i].draw()
    for i in range (10):
        pelletBag[i].draw()
    pygame.draw.circle(screen, (200,0,200), (xPos, yPos),12)
    pygame.display.flip()
#endgameloop
pygame.quit()#this is the end of my code to fully inspect it I reccommend moving your mouse around the screen 