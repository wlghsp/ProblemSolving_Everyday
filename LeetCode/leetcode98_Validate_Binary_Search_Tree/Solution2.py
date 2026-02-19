class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def validate(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)  

        return validate(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    sol = Solution()

    # Test 1: [2,1,3] → True
    #     2
    #    / \
    #   1   3
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    print(sol.isValidBST(root1))  # Expected: True

    # Test 2: [5,1,4,null,null,3,6] → False
    #       5
    #      / \
    #     1   4
    #        / \
    #       3   6
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)
    print(sol.isValidBST(root2))  # Expected: False

    # Test 3: [2,2,2] → False (같은 값은 BST 아님)
    root3 = TreeNode(2)
    root3.left = TreeNode(2)
    root3.right = TreeNode(2)
    print(sol.isValidBST(root3))  # Expected: False
