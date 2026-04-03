"""
235. Lowest Common Ancestor of a BST (Medium)
https://leetcode.com/problems/lowest-common-ancestor-of-a-bst/

Given a binary search tree (BST), find the lowest common ancestor (LCA)
of two given nodes in the BST.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

if __name__ == "__main__":
    sol = Solution()

    # Test 1: root=[6,2,8,0,4,7,9], p=2, q=8 -> 6
    root1 = TreeNode(6)
    root1.left = TreeNode(2)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(7)
    root1.right.right = TreeNode(9)
    p1, q1 = root1.left, root1.right  # 2, 8
    print(sol.lowestCommonAncestor(root1, p1, q1).val)  # Expected: 6

    # Test 2: root=[6,2,8,0,4,7,9], p=2, q=4 -> 2
    p2, q2 = root1.left, root1.left.right  # 2, 4
    print(sol.lowestCommonAncestor(root1, p2, q2).val)  # Expected: 2

    # Test 3: root=[2,1], p=2, q=1 -> 2
    root3 = TreeNode(2)
    root3.left = TreeNode(1)
    p3, q3 = root3, root3.left  # 2, 1
    print(sol.lowestCommonAncestor(root3, p3, q3).val)  # Expected: 2
