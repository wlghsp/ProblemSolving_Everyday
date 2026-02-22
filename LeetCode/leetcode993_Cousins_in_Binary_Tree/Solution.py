from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree(lst, i=0):
    if i >= len(lst) or lst[i] is None:
        return None
    node = TreeNode(lst[i])
    node.left = make_tree(lst, 2*i+1)
    node.right = make_tree(lst, 2*i+2)
    return node

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([(None, root)])
        x_level, y_level = -1, -1
        x_parent, y_parent = 0, 0
        level = 0
        while q:
            for _ in range(len(q)):
                parent, node = q.popleft()

                if parent:
                    if node.val == x:
                        x_level = level
                        x_parent = parent.val
                    if node.val == y:
                        y_level = level
                        y_parent = parent.val
                if x_level != -1 and y_level != -1:
                    q.clear()
                    break
                if node.left:
                    q.append((node, node.left))
                if node.right:
                    q.append((node, node.right))
            level += 1

        return (x_level == y_level and x_parent != y_parent)


if __name__ == "__main__":
    sol = Solution()

    # Test 1: root = [1,2,3,4], x=4, y=3 → False
    # 4는 depth=2, parent=2 / 3는 depth=1 → 깊이 다름
    print(sol.isCousins(make_tree([1, 2, 3, 4]), 4, 3))  # False

    # Test 2: root = [1,2,3,None,4,None,5], x=5, y=4 → True
    # 4는 depth=2, parent=2 / 5는 depth=2, parent=3 → 사촌!
    print(sol.isCousins(make_tree([1, 2, 3, None, 4, None, 5]), 5, 4))  # True

    # Test 3: root = [1,2,3,None,4], x=2, y=3 → False
    # 2,3은 같은 레벨이지만 부모가 같음 (형제) → False
    print(sol.isCousins(make_tree([1, 2, 3, None, 4]), 2, 3))  # False