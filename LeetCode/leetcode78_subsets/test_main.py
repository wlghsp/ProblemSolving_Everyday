from unittest import TestCase

from main import Solution


class TestSolution(TestCase):
    def test_dfs(self):
        sol = Solution()
        self.assertEqual(sorted([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]), sorted(sol.subsets([1,2,3])))

    def test1_dfs(self):
        sol = Solution()
        self.assertEqual(sorted([[],[0]]), sorted(sol.subsets([0])))


