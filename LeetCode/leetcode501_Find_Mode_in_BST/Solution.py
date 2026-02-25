from collections import deque
from typing import Optional, List


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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = {}
        def dfs(node):
            if not node:
                return
            count[node.val] = count.get(node.val, 0) + 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        max_val = max(count.values())
        result = [k for k,v in count.items() if v == max_val]
        return result

if __name__ == "__main__":
    s = Solution()

    root = build_tree([1, None, 2, 2])
    print(s.findMode(root))   # [2]

    root = build_tree([0])
    print(s.findMode(root))   # [0]

    root = build_tree([1, None, 2])
    print(s.findMode(root))   # [1, 2]
