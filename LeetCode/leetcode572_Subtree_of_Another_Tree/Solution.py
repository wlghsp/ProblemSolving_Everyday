class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right
    
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 

if __name__ == "__main__":
    sol = Solution()

    # Test 1: root = [3,4,5,1,2], subRoot = [4,1,2] → True
    #       3
    #      / \
    #     4   5
    #    / \
    #   1   2
    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)

    sub1 = TreeNode(4)
    sub1.left = TreeNode(1)
    sub1.right = TreeNode(2)
    print(sol.isSubtree(root1, sub1))  # Expected: True

    # Test 2: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] → False
    #       3
    #      / \
    #     4   5
    #    / \
    #   1   2
    #  /
    # 0
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)
    root2.left.left.left = TreeNode(0)

    sub2 = TreeNode(4)
    sub2.left = TreeNode(1)
    sub2.right = TreeNode(2)
    print(sol.isSubtree(root2, sub2))  # Expected: False
