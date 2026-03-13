from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        return root

if __name__ == "__main__":
    def build(vals):
        if not vals:
            return None
        nodes = [TreeNode(v) if v is not None else None for v in vals]
        for i in range(len(nodes)):
            if nodes[i]:
                l, r = 2*i+1, 2*i+2
                if l < len(nodes): nodes[i].left = nodes[l]
                if r < len(nodes): nodes[i].right = nodes[r]
        return nodes[0]

    def to_list(root):
        if not root:
            return []
        res, q = [], [root]
        while q:
            node = q.pop(0)
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
        return res

    sol = Solution()

    # Test 1: val=2 → [2,1,3]
    root = build([4, 2, 7, 1, 3])
    print(to_list(sol.searchBST(root, 2)))  # [2, 1, 3]

    # Test 2: val=5 → []
    root = build([4, 2, 7, 1, 3])
    print(to_list(sol.searchBST(root, 5)))  # []
