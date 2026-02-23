from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree(lst, i=0):
    if i >= len(lst) or lst[i] is None:
        return None
    node = TreeNode(lst[i])
    node.left = make_tree(lst, 2*i+1)
    node.right = make_tree(lst, 2*i+2)
    return node

def print_tree(root):
    if not root:
        return []
    result, q = [], deque([root])
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return result

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right  = self.invertTree(root.right), self.invertTree(root.left)
        return root

if __name__ == "__main__":
    sol = Solution()

    # Test 1: root = [4,2,7,1,3,6,9] → [4,7,2,9,6,3,1]
    result = sol.invertTree(make_tree([4, 2, 7, 1, 3, 6, 9]))
    print(print_tree(result))  # [4, 7, 2, 9, 6, 3, 1]

    # Test 2: root = [2,1,3] → [2,3,1]
    result = sol.invertTree(make_tree([2, 1, 3]))
    print(print_tree(result))  # [2, 3, 1]

    # Test 3: root = [] → []
    result = sol.invertTree(None)
    print(print_tree(result))  # []
