from typing import Optional, List
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inordertraversal_helper(root, [])

    def inordertraversal_helper(self, root, lst):
        if root is None:
            return []

        if root.left is not None:
            self.inordertraversal_helper(root.left, lst)

        lst.append(root.val)

        if root.right is not None:
            self.inordertraversal_helper(root.right, lst)

        return lst


sol = Solution()

print(sol)
