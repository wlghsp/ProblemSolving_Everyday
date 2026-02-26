class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pass


if __name__ == "__main__":
    # Test 1: root=[6,2,8,0,4,7,9,null,null,3,5], p=2, q=8 -> 6
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    s = Solution()
    print(s.lowestCommonAncestor(root, root.left, root.right).val)  # 6

    # Test 2: p=2, q=4 -> 2
    print(s.lowestCommonAncestor(root, root.left, root.left.right).val)  # 2
