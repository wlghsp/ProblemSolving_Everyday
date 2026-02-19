class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        def dfs(node, path):
            
            


if __name__ == "__main__":
    sol = Solution()

    # Test 1: [1,2,3,null,5] → ["1->2->5","1->3"]
    #     1
    #    / \
    #   2   3
    #    \
    #     5
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    print(sol.binaryTreePaths(root1))  # ["1->2->5","1->3"]

    # Test 2: [1] → ["1"]
    root2 = TreeNode(1)
    print(sol.binaryTreePaths(root2))  # ["1"]
