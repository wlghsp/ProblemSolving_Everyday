class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()

    # Test 1: [1,2,3,4,5,6] → 6
    #       1
    #      / \
    #     2   3
    #    / \ /
    #   4  5 6
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    print(sol.countNodes(root1))  # Expected: 6

    # Test 2: [] → 0
    print(sol.countNodes(None))   # Expected: 0

    # Test 3: [1] → 1
    print(sol.countNodes(TreeNode(1)))  # Expected: 1
