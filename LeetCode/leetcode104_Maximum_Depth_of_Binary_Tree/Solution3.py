from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)


if __name__ == "__main__":
    sol = Solution()

    # Example 1: [3,9,20,null,null,15,7] -> 3
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(sol.maxDepth(root1))  # Expected: 3

    # Example 2: [1,null,2] -> 2
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    print(sol.maxDepth(root2))  # Expected: 2

    # Example 3: empty tree -> 0
    print(sol.maxDepth(None))  # Expected: 0
