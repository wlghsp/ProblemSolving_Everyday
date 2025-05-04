# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        q = deque()
        q.append((root, targetSum))

        def is_leaf(node):
            return node.left is None and node.right is None

        while q:
            node, total = q.popleft()

            # 리프 노드라도 값이 같은 경우를 찾아야 함
            if is_leaf(node) and node.val == total:
                return True

            if node.left:
                q.append((node.left, total - node.val))
            if node.right:
                q.append((node.right, total - node.val))

        return False

# root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    print(sol.hasPathSum(root, 22)) # True
