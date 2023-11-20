from unittest import TestCase

from main import Solution


class TestSolution(TestCase):
    def test_is_anagram(self):
        sol = Solution()
        self.assertEqual(True, sol.isAnagram("anagram", "nagaram"))

    def test_is_anagram2(self):
        sol = Solution()
        self.assertEqual(False, sol.isAnagram("rat", "car"))

