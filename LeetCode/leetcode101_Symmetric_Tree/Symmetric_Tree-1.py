class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isEqual(a: TreeNode, b: TreeNode) -> bool:
            if a is None or b is None:
                return a == b
            if a.val != b.val:
                return False

            return isEqual(a.left, b.right) and isEqual(a.right, b.left)

        return root is None or isEqual(root.left, root.right)
