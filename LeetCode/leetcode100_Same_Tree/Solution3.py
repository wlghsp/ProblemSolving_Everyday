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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    sol = Solution()

    # Test 1: p = [1,2,3], q = [1,2,3] → True
    print(sol.isSameTree(make_tree([1,2,3]), make_tree([1,2,3])))  # True

    # Test 2: p = [1,2], q = [1,None,2] → False
    print(sol.isSameTree(make_tree([1,2]), make_tree([1,None,2])))  # False

    # Test 3: p = [1,2,1], q = [1,1,2] → False
    print(sol.isSameTree(make_tree([1,2,1]), make_tree([1,1,2])))  # False
