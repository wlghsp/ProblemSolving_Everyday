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
    s = Solution()

    root = build_tree([1, 2, 3, None, 5])
    print(s.binaryTreePaths(root))   # ["1->2->5", "1->3"]

    root = build_tree([1])
    print(s.binaryTreePaths(root))   # ["1"]
