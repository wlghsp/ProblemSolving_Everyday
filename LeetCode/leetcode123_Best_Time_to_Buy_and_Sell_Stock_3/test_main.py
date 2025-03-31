from unittest import TestCase

from main import Solution


class TestSolution(TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(6, sol.maxProfit([3,3,5,0,0,3,1,4]))

    def test_2(self):
        sol = Solution()
        self.assertEqual(4, sol.maxProfit([1,2,3,4,5]))

