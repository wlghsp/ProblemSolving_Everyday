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
        result = []
        max_count = 0
        prev = None
        curr_count = 0
        def inorder(node):
            nonlocal prev
            nonlocal curr_count
            nonlocal max_count
            if not node:
                return 
            inorder(node.left)
            if prev == node.val:
                curr_count += 1
            else:
                prev = node.val
                curr_count = 1

            if max_count < curr_count:
                max_count = curr_count
                result.clear()
                result.append(node.val)
            elif max_count == curr_count:
                result.append(node.val)
            inorder(node.right)
        inorder(root)
        return result


if __name__ == "__main__":
    s = Solution()

    root = build_tree([1, None, 2, 2])
    print(s.findMode(root))   # [2]

    root = build_tree([0])
    print(s.findMode(root))   # [0]

    root = build_tree([1, None, 2])
    print(s.findMode(root))   # [1, 2]
