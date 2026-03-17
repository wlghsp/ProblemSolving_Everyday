from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(node, path):
            path += str(node.val)
            if node and not node.left and not node.right:
                result.append(path)
                return
            if node.left:
                dfs(node.left, path + "->")
            if node.right:
                dfs(node.right, path + "->")

        dfs(root, "")
        return result

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

    s = Solution()
    print(s.binaryTreePaths(build([1, 2, 3, None, 5])))  # ["1->2->5", "1->3"]
    print(s.binaryTreePaths(build([1])))                  # ["1"]
