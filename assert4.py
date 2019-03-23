import unittest

def hello_world():
    return 'hello world'

def create_num_list(length):
    return length

class MyFirstTests(unittest.TestCase):
    import pdb; pdb.set_trace()
    def test_hello(self):
            self.assertEqual(hello_world(), 'hello world')

    def test_custom_num_list(self):
            self.assertEqual(create_num_list(10), 10)

if __name__ == '__main__':
    unittest.main()
