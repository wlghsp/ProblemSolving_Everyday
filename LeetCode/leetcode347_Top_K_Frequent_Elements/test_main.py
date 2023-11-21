from unittest import TestCase

from main import Solution


class TestSolution(TestCase):
    def test_top_k_frequent(self):
        sol = Solution()
        self.assertEqual([1, 2], sol.topKFrequent([1,1,1,2,2,3], 2))

    def test_top_k_frequent2(self):
        sol = Solution()
        self.assertEqual([1], sol.topKFrequent([1], 1))

