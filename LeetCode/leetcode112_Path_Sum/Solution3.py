from collections import deque
from typing import Optional

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

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def isLeaf(node):
            return not node.left and not node.right
        q = deque([(root, targetSum)])

        while q:
            for _ in range(len(q)):
                node, total = q.popleft()

                if isLeaf(node) and node.val == total:
                    return True
                
                if node.left:
                    q.append((node.left, total - node.val))
                if node.right:
                    q.append((node.right, total - node.val))

        return False
if __name__ == "__main__":
    sol = Solution()

    # Test 1: root = [5,4,8,11,None,13,4,7,2,None,None,None,1], targetSum = 22 → True
    print(sol.hasPathSum(make_tree([5,4,8,11,None,13,4,7,2,None,None,None,1]), 22))  # True

    # Test 2: root = [1,2,3], targetSum = 5 → False
    print(sol.hasPathSum(make_tree([1,2,3]), 5))  # False

    # Test 3: root = [], targetSum = 0 → False
    print(sol.hasPathSum(None, 0))  # False
