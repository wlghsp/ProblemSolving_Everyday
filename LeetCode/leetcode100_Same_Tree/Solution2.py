from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])
        while queue:
            n1, n2 = queue.popleft()
            if not n1 and not n2: continue
            if not n1 or not n2: return False
            if n1.val != n2.val: return False
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))
        return True


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Same trees [1,2,3]
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(sol.isSameTree(p1, q1))  # Expected: True

    # Test 2: Different structure [1,2] vs [1,null,2]
    p2 = TreeNode(1, TreeNode(2))
    q2 = TreeNode(1, None, TreeNode(2))
    print(sol.isSameTree(p2, q2))  # Expected: False

    # Test 3: Different values [1,2,1] vs [1,1,2]
    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))
    print(sol.isSameTree(p3, q3))  # Expected: False

    # Test 4: Both empty
    print(sol.isSameTree(None, None))  # Expected: True

    # Test 5: One empty
    print(sol.isSameTree(TreeNode(1), None))  # Expected: False
