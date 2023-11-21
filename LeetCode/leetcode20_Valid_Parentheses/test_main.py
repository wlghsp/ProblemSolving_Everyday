from unittest import TestCase

from main import Solution


class TestSolution(TestCase):
    def test_parentheses(self):
        sol = Solution()
        self.assertEqual(True, sol.isValid("()"))

    def test_parentheses1(self):
        sol = Solution()
        self.assertEqual(True, sol.isValid("()[]{}"))


