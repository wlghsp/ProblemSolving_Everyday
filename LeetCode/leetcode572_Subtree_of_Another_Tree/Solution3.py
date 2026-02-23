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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    sol = Solution()

    # Test 1: root = [3,4,5,1,2], subRoot = [4,1,2] → True
    print(sol.isSubtree(make_tree([3,4,5,1,2]), make_tree([4,1,2])))  # True

    # Test 2: root = [3,4,5,1,2,None,None,None,None,0], subRoot = [4,1,2] → False
    print(sol.isSubtree(make_tree([3,4,5,1,2,None,None,None,None,0]), make_tree([4,1,2])))  # False
