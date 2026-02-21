class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(node, targetSum):
            if node and not node.right and not node.left:
                return node.val == targetSum
            left, right = False, False
            if node.left:
                left = dfs(node.left, targetSum - node.val)
            if node.right:
                right = dfs(node.right, targetSum - node.val)
            
            return left or right
            
        return dfs(root, targetSum)
            

if __name__ == "__main__":
    sol = Solution()
    # [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum=22 → True
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print(sol.hasPathSum(root, 22))  # True

    # [], targetSum=0 → False
    print(sol.hasPathSum(None, 0))   # False

    # [1,2], targetSum=1 → False
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    print(sol.hasPathSum(root2, 1))  # False
