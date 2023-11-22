from unittest import TestCase

from main import Solution


class TestSolution(TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(True, sol.isPalindrome(121))

    def test2(self):
        sol = Solution()
        self.assertEqual(False, sol.isPalindrome(-121))


