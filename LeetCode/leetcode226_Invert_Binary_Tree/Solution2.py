class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.right = left
        root.left = right
        return root
        
        


if __name__ == "__main__":
    sol = Solution()

    def to_list(node):
        if not node:
            return []
        result = []
        queue = [node]
        while queue:
            n = queue.pop(0)
            if n:
                result.append(n.val)
                queue.append(n.left)
                queue.append(n.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result

    # Test 1: [4,2,7,1,3,6,9] → [4,7,2,9,6,3,1]
    #       4              4
    #      / \    →       / \
    #     2   7          7   2
    #    / \ / \        / \ / \
    #   1  3 6  9      9  6 3  1
    root1 = TreeNode(4)
    root1.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root1.right = TreeNode(7, TreeNode(6), TreeNode(9))
    print(to_list(sol.invertTree(root1)))  # [4, 7, 2, 9, 6, 3, 1]

    # Test 2: [2,1,3] → [2,3,1]
    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(to_list(sol.invertTree(root2)))  # [2, 3, 1]

    # Test 3: [] → []
    print(to_list(sol.invertTree(None)))  # []
