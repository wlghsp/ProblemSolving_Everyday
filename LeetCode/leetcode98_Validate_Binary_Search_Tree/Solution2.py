class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        nums = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)
        
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                return False
        
        return True

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
