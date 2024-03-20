import unittest
#from sample import sum_negative, sum_positive

def sum_negative(num1, num2):
    if num1 < 0 and num2 < 0:
        return num1 + num2
    else:
        return None

def sum_positive(num1, num2):
    if num1 > 0 and num2 > 0:
        return num1 + num2
    else:
        return None



class SumTests(unittest.TestCase):

    def test_sum(self):
        self.assertEqual (sum_negative(-5, -5), -10)
        self.assertEqual (sum_negative(5, 2), None)

    def test_sum_positive_ok(self):
        self.assertEqual (sum_positive(2, 2), 4)
        self.assertEqual (sum_positive(-5, -2), None)

  '''
  C:\Users\pmelanah\PycharmProjects\myPythonProject>coverage report -m coverageExample.py
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
coverageExample.py      16     16     0%   1-26
--------------------------------------------------
TOTAL                   16     16     0%

C:\Users\pmelanah\PycharmProjects\myPythonProject>coverage report -m
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
coverageExample.py      16      0   100%
--------------------------------------------------
TOTAL                   16      0   100%

'''
