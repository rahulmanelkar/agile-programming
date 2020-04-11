import unittest
from calcTddProductionCode import *

class SimpleTest(unittest.TestCase):

# ADD
    def testadd1(self):
        self.assertEqual(add(3,5),8)

    def testadd2(self):
        self.assertEqual(add(3.5,5), 8.5)

    def testadd3(self):
        self.assertEqual(add("One", "Two"), "OneTwo")
# SUB
    def testsub4(self):
        self.assertEqual(sub(5, 3), 2)

    def testsub5(self):
        self.assertEqual(sub(5.5, 2.5), 3.0)
# MULTIPLY
    def testMultiply6(self):
        self.assertEqual(multiply (3,2),6)

    def testMultiply7(self):
        self.assertEqual(multiply (3.5,2.5),8.75)
#DiVIDE
    def testDivide8(self):
        self.assertEqual(divide (8,2),4)

    def testDevide9(self):
        self.assertEqual(divide (25.0,5),5.0)

if __name__ == '__main__':
    unittest.main()
