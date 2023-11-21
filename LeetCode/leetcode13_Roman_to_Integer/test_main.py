from unittest import TestCase

from main import Solution


class TestSolution(TestCase):
    def test_romanToInt(self):
        sol = Solution()
        self.assertEqual(58, sol.romanToInt("LVIII"))

    def test_romanToInt1(self):
        sol = Solution()
        self.assertEqual(1994, sol.romanToInt("MCMXCIV"))


