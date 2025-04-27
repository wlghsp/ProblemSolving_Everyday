from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None

        # 중위 왼 -> root -> 오
        def inorder(node):
            if not node:
                return
            inorder(node.left)

            self.count += 1
            if self.count == k:
                self.result = node.val
                return

            inorder(node.right)

        inorder(root)

        return self.result

if __name__ == "__main__":
    sol = Solution()
    root1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    root = TreeNode(5,
                    TreeNode(3,
                             TreeNode(2,
                                      TreeNode(1)
                                      ),
                             TreeNode(4)
                             ),
                    TreeNode(6)
                    )
    print(sol.kthSmallest(root1, 1)) # 1
    print(sol.kthSmallest(root, 3)) # 3
