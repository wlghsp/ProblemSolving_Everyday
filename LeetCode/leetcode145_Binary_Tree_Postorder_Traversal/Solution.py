from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)
        postorder(root)
        return res

if __name__ == "__main__":
    def build(vals):
        if not vals:
            return None
        from collections import deque
        root = TreeNode(vals[0])
        q = deque([root])
        i = 1
        while q and i < len(vals):
            node = q.popleft()
            if i < len(vals) and vals[i] is not None:
                node.left = TreeNode(vals[i])
                q.append(node.left)
            i += 1
            if i < len(vals) and vals[i] is not None:
                node.right = TreeNode(vals[i])
                q.append(node.right)
            i += 1
        return root

    sol = Solution()

    # Example 1: [1,null,2,3] -> [3,2,1]
    root1 = build([1, None, 2, 3])
    print(sol.postorderTraversal(root1))  # Expected: [3, 2, 1]

    # Example 2: [] -> []
    print(sol.postorderTraversal(None))  # Expected: []

    # Example 3: [1] -> [1]
    root3 = build([1])
    print(sol.postorderTraversal(root3))  # Expected: [1]
