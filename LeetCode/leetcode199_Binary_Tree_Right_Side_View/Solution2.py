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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    continue

                if node:
                    level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level:
                result.append(level[-1])
        return result



if __name__ == "__main__":
    s = Solution()

    root = build_tree([1, 2, 3, None, 5, None, 4])
    print(s.rightSideView(root))   # [1, 3, 4]

    root = build_tree([1, None, 3])
    print(s.rightSideView(root))   # [1, 3]

    print(s.rightSideView(None))   # []
