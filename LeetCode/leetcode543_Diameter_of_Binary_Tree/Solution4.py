from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        def dfs(node):
            nonlocal max_len
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            max_len = max(max_len, left + right)
            return max(left, right) + 1
        dfs(root)
        return max_len

if __name__ == "__main__":
    sol = Solution()

    # Test 1: [1,2,3,4,5] → 3
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    print(sol.diameterOfBinaryTree(root1))  # Expected: 3

    # Test 2: [1,2] → 1
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    print(sol.diameterOfBinaryTree(root2))  # Expected: 1
