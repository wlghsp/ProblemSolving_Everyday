class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()

    # Test 1: [3,9,20,null,null,15,7] → True
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
    print(sol.isBalanced(root1))  # True

    # Test 2: [1,2,2,3,3,null,null,4,4] → False
    #         1
    #        / \
    #       2   2
    #      / \
    #     3   3
    #    / \
    #   4   4
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    print(sol.isBalanced(root2))  # False

    # Test 3: [] → True
    print(sol.isBalanced(None))  # True
