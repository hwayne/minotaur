class Entity:

    def __init__(self, x = 0, y = 0):
        self.xpos = x
        self.ypos = y
        self.hist = [(y,x)]
        pass

    def setBoard(self, board):
        self.board = board

    def getpos(self):
        return (self.ypos, self.xpos)

    #Are two entities in same place?
    def isOverlap(self, e):
        return (self.xpos == e.xpos) and (self.ypos == e.ypos)

    #Generic move.
    #Note you can delay with move(0).
    def moveX(self, dist = 1):
        self.xpos += 2*dist
#Seperate moveY for simplicity.
    def moveY(self, dist = 1):
        self.ypos += 2*dist

#Check for collisions.
#A collision is when an entity tries to move into
#A square marked '_' or '|' (a wall)
    def isReachable(self, char):
        return (char == ' ')

    def isOnBoard(self, x = 0, y = 0):
        return(0 <= self.xpos + 2*x <= len(self.board[0])
              and 0 <= self.ypos + 2*y <= len(self.board))

    def updatehist(self):
        self.hist.append((self.ypos,self.xpos))
    #Play a whole turn.
    def turn(self):
        self.moveX(1)
        self.updatehist()


    #undo move. Requires history.
    def undo(self):
        if len(self.hist) > 1: self.hist.pop()
        self.xpos = self.hist[-1][1]
        self.ypos = self.hist[-1][0]

#move back to starting coordinates.
    def reset(self):
        self.hist = [self.hist[0]]
        self.xpos = self.hist[0][1]
        self.ypos = self.hist[0][0]
