import unittest
import entity
import minotaur

class EntityTests(unittest.TestCase):
   
    def setUp(self):
        self.E = entity.Entity(x = 0, y = 0)

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
        self.assertNotEqual(self.E.getpos(), (0,1))

    def testMoveX(self):
        self.E.moveX(1)
        self.assertTrue(self.E.xpos == 1)
        self.E.moveX(-1)
        self.assertTrue(self.E.xpos == 0)

    def testMoveY(self):
        self.E.moveY(1)
        self.assertTrue(self.E.ypos == 1)
        self.E.moveY(-1)
        self.assertTrue(self.E.ypos == 0)

    def testTurn(self):
        F = entity.Entity(5, 8)
        F.turn()
        self.assertTrue(F.xpos == 6)
    
    def testHistory(self):
        F = entity.Entity(x = 2, y = 3)
        F.turn()
        F.turn()
        self.assertEqual(F.hist, [(2,3), (3,3), (4,3)])

    def testUndo(self):
        F = entity.Entity()
        F.turn()
        F.turn()
        F.turn()
        F.undo()
        self.assertEqual(F.hist[-1], (2,0))

    def testReset(self):
        F = entity.Entity()
        F.hist = [(1,2), (5,7), (12, 5)]
        F.reset()
        self.assertEqual(F.hist, [(1,2)])

    def testCollision(self):
        self.assertTrue(self.E.isCollision('_'))
        self.assertTrue(self.E.isCollision('|'))

    def testNotCollision(self):
        self.assertFalse(self.E.isCollision('.'))


class MinotaurTests(unittest.TestCase):
   
    def setUp(self):
        self.M = minotaur.Minotaur(x = 0, y = 0)

    def testBase(self):
        self.assertFalse(False)
    
    def testMoveTwoX(self):
        self.M.turn((2,0))
        self.assertEqual(self.M.getpos(), (2,0))

    def testMoveTwoNegX(self):
        self.M.turn((-2,0))
        self.assertEqual(self.M.getpos(), (-2,0))

    def testMoveTwoY(self):
        self.M.turn((0,2))
        self.assertEqual(self.M.getpos(), (0,2))

    def testMoveOneXOneY(self):
        self.M.turn((1,1))
        self.assertEqual(self.M.getpos(), (1,1))

    def testHist(self):
        self.M.turn((3,6))
        self.M.turn((3,6))
        self.assertEqual(self.M.hist[-1], (3,1))
        self.M.turn((1,1))
        self.assertEqual(self.M.getpos(), (1,1))
if __name__ == "__main__":
   unittest.main()
