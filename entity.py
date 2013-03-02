class Entity:

    def __init__(self, x = 0, y = 0):
        self.xpos = x
        self.ypos = y
        self.hist = [(x,y)]
        pass

    def getpos(self):
        return (self.xpos, self.ypos)
    #Are two entities in same place?
    def isOverlap(self, e):
        return (self.xpos == e.xpos) and (self.ypos == e.ypos)

    #Generic move.
    #Note you can delay with move(0).
    def moveX(self, dist = 1):
        self.xpos += dist
#Seperate moveY for simplicity.
    def moveY(self, dist = 1):
        self.ypos += dist

#Check for collisions.
#A collision is when an entity tries to move into
#A square marked '_' or '|' (a wall)
    def isCollision(self, char):
        return (char == '_' or char == '|')

    def updatehist(self):
        self.hist.append((self.xpos,self.ypos))
    #Play a whole turn.
    def turn(self):
        self.moveX(1)
        self.updatehist()


    #undo move. Requires history.
    def undo(self):
        self.hist.pop()
    
#move back to starting coordinates.
    def reset(self):
        self.hist = [self.hist[0]]
