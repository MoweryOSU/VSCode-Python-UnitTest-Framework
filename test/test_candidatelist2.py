import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import candidatelist2

class TestCandidateList2(unittest.TestCase):

    def setUp(self):
        test = 42

    def tearDown(self):
        test = 43

    # def test_verifyCandidateListEmpty(self):
    #     candidatelist.initCandidateList()
    #     for index, value in enumerate(candidatelist.getCandidateList()):
    #         self.assertEqual(value, candidatelist.invalidValue)

if __name__ == '__main__':
    unittest.main()
