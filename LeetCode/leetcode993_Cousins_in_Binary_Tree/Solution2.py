from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()

    # Example 1: root = [1,2,3,4], x = 4, y = 3
    # Expected: False
    root = build_tree([1, 2, 3, 4])
    print(sol.isCousins(root, 4, 3))

    # Example 2: root = [1,2,3,None,4,None,5], x = 5, y = 4
    # Expected: True
    root = build_tree([1, 2, 3, None, 4, None, 5])
    print(sol.isCousins(root, 5, 4))

    # Example 3: root = [1,2,3,None,4], x = 2, y = 3
    # Expected: False
    root = build_tree([1, 2, 3, None, 4])
    print(sol.isCousins(root, 2, 3))
