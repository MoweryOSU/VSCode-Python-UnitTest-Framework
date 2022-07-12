import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import candidatelist

class TestCandidateList(unittest.TestCase):

    def test_verifyCandidateListEmpty(self):
        candidatelist.initCandidateList()
        for index, value in enumerate(candidatelist.getCandidateList()):
            self.assertEqual(value, candidatelist.invalidValue)

    def test_verifyEmptyCandidateListHasZeroValidCandidates(self):
        candidatelist.initCandidateList()
        self.assertEqual(0, candidatelist.GetNumOfValidCandidates())

    def test_verifyMaximumCandidateListSize(self):
        candidatelist.initCandidateList()
        self.assertEqual(len(candidatelist.getCandidateList()), candidatelist.GetMaxNumCandidates())

    def test_AddCandidateAndVerifyListSize(self):
        candidatelist.initCandidateList()
        candidatelist.AddCandidate(42)
        self.assertEqual(1, candidatelist.GetNumOfValidCandidates())

    def test_AddCandidateAndVerifyListSizeAndBestCandidate(self):
        candidatelist.initCandidateList()
        candidatelist.AddCandidate(42)
        self.assertEqual(1, candidatelist.GetNumOfValidCandidates())
        self.assertEqual(42, candidatelist.GetNextBestCandidate())

    def test_AddTwoCandidateAndVerifyListSizeAndBestCandidates(self):
        candidatelist.initCandidateList()
        candidatelist.AddCandidate(42)
        candidatelist.AddCandidate(20)
        self.assertEqual(2, candidatelist.GetNumOfValidCandidates())
        self.assertEqual(20, candidatelist.GetNextBestCandidate())
        self.assertEqual(42, candidatelist.GetNextBestCandidate())

    def test_AddSevenCandidateAndVerifyListSizeAndBestCandidates(self):
        candidatelist.initCandidateList()
        candidatelist.AddCandidate(42)
        candidatelist.AddCandidate(20)
        candidatelist.AddCandidate(19)
        candidatelist.AddCandidate(18)
        candidatelist.AddCandidate(23)
        candidatelist.AddCandidate(15)
        candidatelist.AddCandidate(32)
        self.assertEqual(6, candidatelist.GetNumOfValidCandidates())
        self.assertEqual(15, candidatelist.GetNextBestCandidate())
        self.assertEqual(18, candidatelist.GetNextBestCandidate())
        self.assertEqual(19, candidatelist.GetNextBestCandidate())
        self.assertEqual(20, candidatelist.GetNextBestCandidate())
        self.assertEqual(23, candidatelist.GetNextBestCandidate())
        self.assertEqual(32, candidatelist.GetNextBestCandidate())
        self.assertEqual(32, candidatelist.GetNextBestCandidate())


if __name__ == '__main__':
    unittest.main()
