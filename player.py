import entity

class Player(entity.Entity):


    def turn(self, command):
        rowmove = 0
        colmove = 0

        if command == "A":
           colmove = -1
        elif command == "D": 
           colmove = 1 
        elif command == 'W':
           rowmove = -1
        elif command == "S":
           rowmove = 1
        elif command == " ":
            self.updatehist()
            return True

        else: return False #invalid commands

        if self.isOnBoard(x = colmove,y = rowmove): 
            char = self.board[self.ypos+rowmove][(self.xpos+colmove)]
            if self.isReachable(char):
                 self.moveX(colmove)
                 self.moveY(rowmove)
                 self.updatehist()
                 return True
        return False
