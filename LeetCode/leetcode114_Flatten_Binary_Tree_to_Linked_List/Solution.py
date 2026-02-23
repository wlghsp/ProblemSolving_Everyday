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

def print_linked(root):
    result = []
    while root:
        result.append(root.val)
        root = root.right
    return result

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        nodes = []
        def preorder(node):
            if not node:
                return 
            nodes.append(node)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
    
        for i in range(1, len(nodes)):
            root.right = nodes[i]
            root.left = None
            root = root.right


if __name__ == "__main__":
    sol = Solution()

    # Test 1: [1,2,5,3,4,None,6] → [1,None,2,None,3,None,4,None,5,None,6]
    root = make_tree([1,2,5,3,4,None,6])
    sol.flatten(root)
    print(print_linked(root))  # [1, 2, 3, 4, 5, 6]

    # Test 2: [] → []
    root = None
    sol.flatten(root)
    print(print_linked(root))  # []

    # Test 3: [0] → [0]
    root = make_tree([0])
    sol.flatten(root)
    print(print_linked(root))  # [0]
