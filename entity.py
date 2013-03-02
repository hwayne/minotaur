class Entity:

    def __init__(self, x = 0, y = 0):
        self.xpos = x
        self.ypos = y
        self.hist = [(x,y)]
        pass

    #Are two entities in same place?
    def isOverlap(self, e):
        return (self.xpos == e.xpos) and (self.ypos == e.ypos)

    #Generic move.
    #Note you can delay with move(0).
    def move(self, dist = 0, xmove = True ):
        if xmove: self.xpos += dist
        else: self.ypos += dist
    #Play a whole turn.
    def turn(self, dist = 0, xmove = True):
        self.move(dist, xmove)
        self.hist.append((self.xpos,self.ypos))

    #undo move. Requires history.
    def undo(self):
        self.hist.pop()
    
#move back to starting coordinates.
    def reset(self):
        self.hist = [self.hist[0]]
