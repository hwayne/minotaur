import unittest
import entity
import minotaur
import player

class EntityTests(unittest.TestCase):
   
    def setUp(self):
        self.E = entity.Entity(x = 0, y = 0)
        self.E.setBoard([['.', ' ', '.'], ['.', '|', '.']])
    def testBase(self):
        self.assertFalse(False)

    def testExists(self):
        self.assertIsInstance(self.E, entity.Entity)
    
    def testOverlap(self):
        F = entity.Entity(x = 0, y = 0)
        self.assertTrue(self.E.isOverlap(F))
        
    def testNotOverlap(self):
        F = entity.Entity(x = 1, y = 2)
        self.assertFalse(self.E.isOverlap(F))

    def testGetPos(self):
        self.assertEqual(self.E.getpos(), (0,0))

    def testNotGetPos(self):
        self.assertNotEqual(self.E.getpos(), (1,0))
    def testSetMap(self):
        self.E.setBoard(['.',' ','.'])
        self.assertEqual(self.E.board, ['.', ' ', '.'])
    def testNotSetMap(self):
        self.E.setBoard(['.', '|', '.'])
        self.assertNotEqual(self.E.board, ['.', ' ', '.'])
    def testMoveX(self):
        self.E.moveX(1)
        self.assertTrue(self.E.xpos == 2)
        self.E.moveX(-1)
        self.assertTrue(self.E.xpos == 0)

    def testMoveY(self):
        self.E.moveY(1)
        self.assertTrue(self.E.ypos == 2)
        self.E.moveY(-1)
        self.assertTrue(self.E.ypos == 0)

    def testTurn(self):
        F = entity.Entity(5, 8)
        F.turn()
        self.assertTrue(F.xpos == 7)
    
    def testHistory(self):
        F = entity.Entity(x = 2, y = 3)
        F.turn()
        F.turn()
        self.assertEqual(F.hist, [(3,2), (3,4), (3,6)])

    def testUndo(self):
        F = entity.Entity()
        F.turn()
        F.turn()
        F.turn()
        F.undo()
        self.assertEqual(F.hist[-1], (0,4))

    def testReset(self):
        F = entity.Entity()
        F.hist = [(2,1), (7,5), (12, 5)]
        F.reset()
        self.assertEqual(F.hist, [(2,1)])

    def testReachable(self):
        self.assertFalse(self.E.isReachable('+'))
        self.assertFalse(self.E.isReachable('_'))

    def testNotReachable(self):
        self.assertTrue(self.E.isReachable(' '))

    def testOnBoard(self):
        self.assertTrue(self.E.isOnBoard(1))
    def testNotOnBoard(self):
        self.assertFalse(self.E.isOnBoard(-1))
        self.assertFalse(self.E.isOnBoard(0, 2))

class MinotaurTests(unittest.TestCase):
   
    def setUp(self):
        self.M = minotaur.Minotaur(x = 0, y = 0)
        self.mapOne = [['.', ' ']*20,[' ', ' ']*20]*20
        self.M.setBoard(self.mapOne)


    def testBase(self):
        self.assertFalse(False)
    
    def testMoveOneX(self):
        self.M.turn((0,2))
        self.assertEqual(self.M.getpos(), (0,2))

    def testMoveTwoX(self):
        self.M.turn((0,4))
        self.assertEqual(self.M.getpos(), (0,4))

    def testMoveTwoNegX(self):
        self.M.turn((-0,4))
        self.assertEqual(self.M.getpos(), (-0,4))

    def testMoveTwoY(self):
        self.M.turn((4,0))
        self.assertEqual(self.M.getpos(), (4,0))
  
    def testMoveOneXOneY(self):
        self.M.turn((2,2))
        self.assertEqual(self.M.getpos(), (2,2))
    
    def testBlockX(self):
        self.M.setBoard([['.','|','.']])
        self.M.turn((0,2))
        self.assertEqual(self.M.getpos(), (0,0))
    
    def testBlockY(self):
        self.M.setBoard([['.'],['_'],['.']])
        self.M.turn((2,0))
        self.assertEqual(self.M.getpos(), (0,0))
    def testBlockOOB(self):
        self.M.setBoard([['.','|','.', ' ']])
        self.M.turn((0,-3))
        self.assertEqual(self.M.getpos(), (0,0))
    
#Will the minotaur walk into a trap?
    def testTrapMinotaur(self):
        self.M.setBoard([['.',' ','.',' ','.'],
                         [' ',' ',' ',' ','-'],
                         ['.',' ','.',' ','.']])
        self.M.turn((2,4))
        self.M.turn((2,4))
        self.assertEqual(self.M.getpos(), (0,4))

#Will the minotaur navigate around obstacles?
#IE, will he change course?
    def testDivertMinotaur(self):
        self.M.setBoard([['.','|','.',' ','.'],
                         [' ',' ',' ',' ','-'],
                         ['.',' ','.',' ','.']])
        self.M.turn((2,4))
        self.assertEqual(self.M.getpos(), (2,2))

    def testHist(self):
        self.M.turn((12,6))
        self.M.turn((12,6))
        self.assertEqual(self.M.hist[-1], (2,6))
        self.M.turn((2,2))
        self.assertEqual(self.M.getpos(), (2,2))

class PlayerTests(unittest.TestCase):
   
    def setUp(self):
        self.P = player.Player(x = 0, y = 0)
        self.P.setBoard([['.', ' ', '.'],[' ']*3, ['.', '|', '.']])

    def testBase(self):
        self.assertFalse(False)

if __name__ == "__main__":
   unittest.main()
