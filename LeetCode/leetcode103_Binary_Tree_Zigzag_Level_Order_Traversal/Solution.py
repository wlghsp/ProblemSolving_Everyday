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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        q = deque([root])
        i = 0
        while q:
            level = deque()
            for _ in range(len(q)):
                node = q.popleft()
                
                if node:
                    if i % 2 == 0:
                        level.append(node.val)
                    else:
                        level.appendleft(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if level:
                result.append(list(level))
            i += 1
        return result



if __name__ == "__main__":
    s = Solution()

    root = build_tree([3, 9, 20, None, None, 15, 7])
    print(s.zigzagLevelOrder(root))   # [[3], [20, 9], [15, 7]]

    root = build_tree([1])
    print(s.zigzagLevelOrder(root))   # [[1]]

    print(s.zigzagLevelOrder(None))   # []