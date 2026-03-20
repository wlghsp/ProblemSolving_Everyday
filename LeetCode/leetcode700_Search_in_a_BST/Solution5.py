from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while curr:
            if curr.val == val:
                return curr
            elif curr.val < val:
                curr = curr.right
            elif curr.val > val:
                curr = curr.left
        return None

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

    def to_list(node):
        if not node: return []
        return [node.val] + to_list(node.left) + to_list(node.right)

    root = build([4, 2, 7, 1, 3])
    print(to_list(Solution().searchBST(root, 2)))  # [2, 1, 3]
    print(to_list(Solution().searchBST(root, 5)))  # []
