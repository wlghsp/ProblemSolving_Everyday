from unittest import TestCase

from main import Solution


class TestSolution(TestCase):
    def test_add_binary(self):
        sol = Solution()
        self.assertEqual("100", sol.addBinary("11", "1"))

    def test_add_binary2(self):
        sol = Solution()
        self.assertEqual("10101", sol.addBinary("1010", "1011"))

    def test_add_binary3(self):
        sol = Solution()
        self.assertEqual("0", sol.addBinary("0", "0"))
