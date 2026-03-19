from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def preorder(node):
            if not node: 
                return
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return result


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


if __name__ == "__main__":
    s = Solution()
    print(s.preorderTraversal(build([1, None, 2, None, None, 3])))  # [1, 2, 3]
    print(s.preorderTraversal(build([])))                           # []
    print(s.preorderTraversal(build([1])))                          # [1]
