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
            if self.xpos != target[1]:
                move = (self.xpos < target[1])*2 - 1#bool is 0 or 1, so move is -1 or +1
                if self.isOnBoard(x = move):
                    char = self.board[self.ypos][(self.xpos + move)] 
                    if self.isReachable(char):
                        self.moveX(move)
                        continue #if we move horiz, no need to vert

            if self.ypos != target[0]:
                move = (self.ypos < target[0])*2 - 1
                char = self.board[self.ypos+move][self.xpos] 
                if self.isOnBoard(y = move):
                    if self.isReachable(char):
                        self.moveY(move)
        self.updatehist()
