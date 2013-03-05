import entity

class Player(entity.Entity):


    def turn(self, command):
        valid = True #catch invalid commands
        if self.xpos != target[1]:
                move = (self.xpos < target[1])*2 - 1#bool is 0 or 1, so move is -1 or +1
                char = self.board[self.ypos][(self.xpos + move)] 
                if self.isReachable(char) and self.isOnBoard(x = move):
                    self.moveX(move)
                    continue #if we move horiz, no need to vert

        else: valid = False;
        if valid: self.updatehist()
        
        return valid
