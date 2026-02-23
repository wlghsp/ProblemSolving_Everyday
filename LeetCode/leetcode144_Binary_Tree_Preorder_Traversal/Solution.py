from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        st = [root]
        while st:
            node = st.pop()
            res.append(node.val)

            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
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

    # Example 1: [1,null,2,3] -> [1,2,3]
    root1 = build([1, None, 2, 3])
    print(sol.preorderTraversal(root1))  # Expected: [1, 2, 3]

    # Example 2: [] -> []
    print(sol.preorderTraversal(None))  # Expected: []

    # Example 3: [1] -> [1]
    root3 = build([1])
    print(sol.preorderTraversal(root3))  # Expected: [1]
