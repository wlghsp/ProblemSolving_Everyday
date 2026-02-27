from typing import Optional
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> list[list[int]]:
        nodes = []
        def dfs(node, c, r):
            if not node:
                return
            nodes.append((c, r, node.val))
            dfs(node.left, c - 1, r + 1)
            dfs(node.right, c + 1, r + 1)    
        
        dfs(root, 0, 0)
        
        nodes.sort()
        
        result = []
        i = 0
        while i < len(nodes):
            cols = []
            c, _, _ = nodes[i]
            while i < len(nodes) and c == nodes[i][0]:
                cols.append(nodes[i][2])
                i += 1
            result.append(cols)
        return result    

if __name__ == "__main__":
    s = Solution()

    # Example 1: root = [3,9,20,null,null,15,7]
    # Expected: [[9],[3,15],[20],[7]]
    root = build_tree([3, 9, 20, None, None, 15, 7])
    print(s.verticalTraversal(root))

    # Example 2: root = [1,2,3,4,5,6,7]
    # Expected: [[4],[2],[1,5,6],[3],[7]]
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    print(s.verticalTraversal(root))

    # Example 3: root = [1,2,3,4,6,5,7]
    # Expected: [[4],[2],[1,5,6],[3],[7]]
    root = build_tree([1, 2, 3, 4, 6, 5, 7])
    print(s.verticalTraversal(root))
