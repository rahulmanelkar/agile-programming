import unittest
from calcTddProductionCode import *

class SimpleTest(unittest.TestCase):
    def testadd(self):
        self.assertEqual(add(3,5),8)

    def testadd1(self):
        self.assertEqual(add(3.5,5), 8.5)

    def testadd2(self):
        self.assertEqual(add("One", "Two"), "OneTwo")

if __name__ == '__main__':
    unittest.main()
