class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.min_depth = float('inf')

        def dfs(node, depth):
            if not node:
                return depth
            if node and (not node.left and not node.right):
                self.min_depth = min(self.min_depth, depth + 1)
            left, right = 0, 0
            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)
            return min(left, right) + 1
        dfs(root, 0)
        return self.min_depth
    
if __name__ == "__main__":
    sol = Solution()

    # Test 1: [3,9,20,null,null,15,7] → 2
    #       3
    #      / \
    #     9  20
    #        / \
    #       15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(sol.minDepth(root1))  # 2

    # Test 2: [2,null,3,null,4,null,5,null,6] → 5
    #   2
    #    \
    #     3
    #      \
    #       4
    #        \
    #         5
    #          \
    #           6
    root2 = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.right = TreeNode(4)
    root2.right.right.right = TreeNode(5)
    root2.right.right.right.right = TreeNode(6)
    print(sol.minDepth(root2))  # 5

    # Test 3: [] → 0
    print(sol.minDepth(None))  # 0

    # Test 4: [1] → 1
    print(sol.minDepth(TreeNode(1)))  # 1
