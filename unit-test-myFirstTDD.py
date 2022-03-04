mycode.py
-------------

def hello_world():
    return ("Hello World1")
    #pass
    
    
mytests.py
---------------

import unittest
from mycode import *

class MyFirstTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(),'Hello World')

if __name__ == '__main__':
    unittest.main()
