from collections import deque
from typing import Optional


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


def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root

        while current:
            if current.val == val:
                return current
            
            if current.val < val:
                current = current.right
            elif current.val > val:
                current = current.left
        
        return None


if __name__ == "__main__":
    s = Solution()

    root = build_tree([4, 2, 7, 1, 3])
    print(tree_to_list(s.searchBST(root, 2)))  # [2, 1, 3]

    root = build_tree([4, 2, 7, 1, 3])
    print(tree_to_list(s.searchBST(root, 5)))  # []

    root = build_tree([1])
    print(tree_to_list(s.searchBST(root, 1)))  # [1]
