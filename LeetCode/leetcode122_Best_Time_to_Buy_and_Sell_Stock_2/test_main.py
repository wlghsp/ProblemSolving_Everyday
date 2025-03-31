from unittest import TestCase

from main import Solution


class TestSolution(TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(7, sol.maxProfit([7,1,5,3,6,4]))

    def test_2(self):
        sol = Solution()
        self.assertEqual(0, sol.maxProfit([7,6,4,3,1]))

