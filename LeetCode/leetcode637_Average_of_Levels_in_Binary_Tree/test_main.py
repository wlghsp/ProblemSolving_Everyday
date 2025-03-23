from unittest import TestCase

from LeetCode.leetcode637_Average_of_Levels_in_Binary_Tree.main import TreeNode, Solution


class TestSolution(TestCase):
    def test_average_of_levels(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        expected = [3.0,14.5,11.0]
        sol = Solution()
        result = sol.averageOfLevels(root)

        self.assertEqual(result, expected)
