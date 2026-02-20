from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()

                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level:
                result.append(level[-1])
        return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: [1,2,3,null,5,null,4] → [1,3,4]
    #       1
    #      / \
    #     2   3
    #      \    \
    #       5    4
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)
    print(sol.rightSideView(root1))  # [1, 3, 4]

    # Test 2: [1,null,3] → [1,3]
    root2 = TreeNode(1)
    root2.right = TreeNode(3)
    print(sol.rightSideView(root2))  # [1, 3]

    # Test 3: [] → []
    print(sol.rightSideView(None))   # []
