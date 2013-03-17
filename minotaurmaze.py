import entity
import minotaur
import player
from getch import *
from itertools import product
import os 
from sys import argv

class Game:

    def __init__(self, boardfile):
        board = file(boardfile).read()
        self.board = [list(x) for x in board.split('\n')]
        self.board.remove([])

        for x in product(range(0, len(self.board), 2), range(0, len(self.board[0]), 2)):
            if self.board[x[0]][x[1]] == 'M':
                self.minotaur = minotaur.Minotaur(y= x[0], x = x[1])
                self.board[x[0]][x[1]] = '.'
                continue

            if self.board[x[0]][x[1]] == '@':
                self.player = player.Player(y = x[0], x = x[1])
                self.board[x[0]][x[1]] = '.'
                continue

            if self.board[x[0]][x[1]] == 'E':
                self.exit = (x[0], x[1])
                continue

        self.minotaur.setBoard(self.board)
        self.player.setBoard(self.board)

    def displayBoard(self):
        _ = os.system('clear')
        p = self.player.getpos()
        m = self.minotaur.getpos()
        self.board[p[0]][p[1]] = '@'
        self.board[m[0]][m[1]] = 'M'
        for row in self.board:
            print reduce(lambda x,y: x+y, row)
        self.board[p[0]][p[1]] = '.'
        self.board[m[0]][m[1]] = '.'
        self.board[self.exit[0]][self.exit[1]] = 'E'
 
    def processMove(self, g):
#R starts game over
         if g == "R":
            self.minotaur.reset()
            self.player.reset()
            return True
#U undos one move for both player and minotaur
         elif g == "U":
            self.minotaur.undo()
            self.player.undo()
            return True

         else: 
             if self.player.turn(g):
                self.minotaur.turn(self.player.getpos())
                return True
             return False

    def loseGame(self):
        print "You lose! (R)eset, (U)ndo, (Q)uit?"
        while True:
            g = getch().upper()
            if g in "RUQ": return g

    def winGame(self):
        print "You win! (R)eset, (U)ndo, (Q)uit?"
        while True:
            g = getch().upper()
            if g in "RUQ": return g

    def playGame(self):
        g = ''
        while g != "Q":
            if self.player.isOverlap(self.minotaur):
               g = self.loseGame()
            elif self.player.getpos() == self.exit:
               g = self.winGame()
            else: g = getch().upper()
            
            if self.processMove(g):
               self.displayBoard()

if __name__ == "__main__":
    if not argv[1].startswith("mazes/"):
        argv[1] = "mazes/" + argv[1]
    G = Game(argv[1])
    G.displayBoard()
    G.playGame()
