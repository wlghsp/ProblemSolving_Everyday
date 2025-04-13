## Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')

        # 중위순회하면 오름 차순 왼쪽 루트 오른쪽
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val

            inorder(node.right)
        inorder(root)

        return self.min_diff


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    print(sol.getMinimumDifference(root)) # 1

