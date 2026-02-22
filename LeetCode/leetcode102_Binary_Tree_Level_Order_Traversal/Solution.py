from typing import Optional, List
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()

                if not node: continue

                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level:
                result.append(level)    

        return result

if __name__ == "__main__":
    sol = Solution()

    # Test 1: root = [3,9,20,None,None,15,7] → [[3],[9,20],[15,7]]
    print(sol.levelOrder(make_tree([3, 9, 20, None, None, 15, 7])))  # [[3],[9,20],[15,7]]

    # Test 2: root = [1] → [[1]]
    print(sol.levelOrder(make_tree([1])))  # [[1]]

    # Test 3: root = [] → []
    print(sol.levelOrder(None))  # []
