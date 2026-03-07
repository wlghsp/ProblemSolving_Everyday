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

    # Test 1: [3,9,20,null,null,15,7] → 3
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(sol.maxDepth(root))  # 3

    # Test 2: [1,null,2] → 2
    root2 = TreeNode(1, None, TreeNode(2))
    print(sol.maxDepth(root2))  # 2

    # Test 3: None → 0
    print(sol.maxDepth(None))  # 0
