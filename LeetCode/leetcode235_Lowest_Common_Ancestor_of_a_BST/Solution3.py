class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        both_left = p.val < root.val and q.val < root.val
        both_right = p.val > root.val and q.val > root.val

        if both_left:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if both_right:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root



if __name__ == "__main__":
    # Tree:      6
    #          /   \
    #         2     8
    #        / \   / \
    #       0   4 7   9
    #          / \
    #         3   5

    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    s = Solution()

    p, q = root.left, root.right  # 2, 8
    print(s.lowestCommonAncestor(root, p, q).val)  # 6

    p, q = root.left, root.left.right  # 2, 4
    print(s.lowestCommonAncestor(root, p, q).val)  # 2
