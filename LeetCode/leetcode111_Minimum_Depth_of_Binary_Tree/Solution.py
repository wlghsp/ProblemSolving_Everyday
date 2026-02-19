class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # 노드가 없음 길이 0 
            if not node:
                return 0          
            left = dfs(node.left)
            right = dfs(node.right)
            # 왼쪽 자식 없으면 오른쪽만 봄
            if not node.left:
                return right + 1
            # 오른쪽 자식 없으면 왼쪽만 봄
            if not node.right:
                return left + 1
            # 둘 다 있으면 더 짧은 쪽 
            return min(left, right) + 1
        return dfs(root)


if __name__ == "__main__":
    sol = Solution()

    # Test 1: [3,9,20,null,null,15,7] → 2
    #       3
    #      / \
    #     9  20
    #        / \
    #       15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(sol.minDepth(root1))  # 2

    # Test 2: [2,null,3,null,4,null,5,null,6] → 5
    #   2
    #    \
    #     3
    #      \
    #       4
    #        \
    #         5
    #          \
    #           6
    root2 = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.right = TreeNode(4)
    root2.right.right.right = TreeNode(5)
    root2.right.right.right.right = TreeNode(6)
    print(sol.minDepth(root2))  # 5

    # Test 3: [] → 0
    print(sol.minDepth(None))  # 0

    # Test 4: [1] → 1
    print(sol.minDepth(TreeNode(1)))  # 1
