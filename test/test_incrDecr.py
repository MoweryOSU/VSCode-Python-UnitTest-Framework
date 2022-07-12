import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import inc_dec
class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(inc_dec.increment(3), 4)

    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(5), 4)

if __name__ == '__main__':
    unittest.main()
