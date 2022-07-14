import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import candidatelist2

class TestCandidateList2(unittest.TestCase):

    # def setUp(self):
    #     test = 42

    # def tearDown(self):
    #     test = 43

    def test_createEmptyCandidateListAndVerify(self):
        testlist = candidatelist2.CandidateList2(0)
        self.assertEqual(0, testlist.getListSize())

    def test_createNonEmptyCandidateListAndVerify(self):
        testlist = candidatelist2.CandidateList2(1)
        self.assertEqual(1, testlist.getListSize())

    def test_createBigNonEmptyCandidateListAndVerifyInvalidCandidates(self):
        testlist = candidatelist2.CandidateList2(10)
        self.assertEqual(10, testlist.getListSize())
        for index in range(testlist.getListSize()):
            self.assertEqual(0xFFFF, testlist.getCandidate(index))


if __name__ == '__main__':
    unittest.main()
