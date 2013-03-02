import entity

class Minotaur(entity.Entity):

    '''The minotaur moves towards the player. It gets
    Two moves per turn. for each move it first tries
    to move horizontally, then it tries to move
    vertically. If it can't do either, it skips that move.
    It always takes the most direct route and cannot
    move away from the player, ever.'''

    def turn(self, target):
        for i in range(2):
            if self.xpos != target[0]:
                move = (self.xpos < target[0])*2 - 1
                self.moveX(move)
            elif self.ypos != target[1]:
                move = (self.ypos < target[1])*2 - 1
                self.moveY(move)
        self.updatehist()
