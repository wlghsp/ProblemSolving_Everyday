from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_num):
            if not node:
                return 0
            curr_num = curr_num * 10 + node.val
            if not node.left and not node.right:
                return curr_num
            return dfs(node.left, curr_num) + dfs(node.right, curr_num)
        return dfs(root, 0)



if __name__ == "__main__":
    # 트리 구성
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution()
    print(sol.sumNumbers(root))  # 결과: 262