class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        if root and not root.left and not root.right:
            targetSum -= root.val
            return targetSum == 0
       
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
    

if __name__ == "__main__":
    sol = Solution()

    # Test 1: [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22 → True
    #         5
    #        / \
    #       4   8
    #      /   / \
    #     11  13   4
    #    /  \       \
    #   7    2       1
    root1 = TreeNode(5)
    root1.left = TreeNode(4)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(11)
    root1.left.left.left = TreeNode(7)
    root1.left.left.right = TreeNode(2)
    root1.right.left = TreeNode(13)
    root1.right.right = TreeNode(4)
    root1.right.right.right = TreeNode(1)
    print(sol.hasPathSum(root1, 22))  # Expected: True

    # Test 2: [1,2,3], targetSum = 5 → False
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    print(sol.hasPathSum(root2, 5))  # Expected: False

    # Test 3: root = [], targetSum = 0 → False
    print(sol.hasPathSum(None, 0))  # Expected: False