# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: [3, 9, 20, null, null, 15, 7]
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(f"Test 1: {sol.maxDepth(root1)}")  # Expected: 3

    # Test case 2: [2, null, 3]
    #     2
    #      \
    #       3
    root2 = TreeNode(2)
    root2.right = TreeNode(3)
    print(f"Test 2: {sol.maxDepth(root2)}")  # Expected: 2

    # Test case 3: empty tree
    root3 = None
    print(f"Test 3: {sol.maxDepth(root3)}")  # Expected: 0

    # Test case 4: single node
    root4 = TreeNode(1)
    print(f"Test 4: {sol.maxDepth(root4)}")  # Expected: 1
