from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pass


if __name__ == "__main__":
    sol = Solution()

    def print_tree(node):
        if not node:
            return []
        from collections import deque
        res, q = [], deque([node])
        while q:
            n = q.popleft()
            if n:
                res.append(n.val)
                q.append(n.left)
                q.append(n.right)
            else:
                res.append(None)
        while res and res[-1] is None:
            res.pop()
        print(res)

    # Test 1: [4,2,7,1,3,6,9] → [4,7,2,9,6,3,1]
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    print_tree(sol.invertTree(root))

    # Test 2: [2,1,3] → [2,3,1]
    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    print_tree(sol.invertTree(root2))

    # Test 3: None → []
    print_tree(sol.invertTree(None))
