from unittest import TestCase

from main import Solution


class TestSolution(TestCase):
    def test_three_sum(self):
        sol = Solution()
        self.assertEqual([[-1,-1,2],[-1,0,1]], sol.threeSum([-1,0,1,2,-1,-4]))

