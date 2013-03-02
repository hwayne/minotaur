import unittest
import entity

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

    def testMoveX(self):
        self.E.move(1)
        self.assertTrue(self.E.xpos == 1)
        self.E.move(-1)
        self.assertTrue(self.E.xpos == 0)

    def testMoveY(self):
        self.E.move(1, False)
        self.assertTrue(self.E.ypos == 1)
        self.E.move(-1, False)
        self.assertTrue(self.E.ypos == 0)

    def testTurn(self):
        F = entity.Entity(5, 8)
        F.turn(1, True)
        self.assertTrue(F.xpos == 6)
    
    def testHistory(self):
        F = entity.Entity(x = 2, y = 3)
        F.turn(1, True)
        F.turn(-1, False)
        self.assertEqual(F.hist, [(2,3), (3,3), (3,2)])

    def testUndo(self):
        F = entity.Entity()
        F.turn(1, True)
        F.turn(4, False)
        F.turn(3, True)
        F.undo()
        self.assertEqual(F.hist[-1], (1,4))

    def testReset(self):
        F = entity.Entity()
        F.hist = [(1,2), (5,7), (12, 5)]
        F.reset()
        self.assertEqual(F.hist, [(1,2)])
if __name__ == "__main__":
   unittest.main()
