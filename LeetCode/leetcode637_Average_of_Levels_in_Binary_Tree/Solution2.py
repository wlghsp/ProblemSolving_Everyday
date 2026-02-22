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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # BFS 레벨 순회
        result = []
        queue = deque([root])

        while queue:
            level_sum = 0
            level_size = 0
            for _ in range(len(queue)):
                node = queue.popleft()

                level_size += 1
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_sum / level_size)

        return result

if __name__ == "__main__":
    sol = Solution()

    # Test 1: root = [3,9,20,None,None,15,7] → [3.0, 14.5, 11.0]
    print(sol.averageOfLevels(make_tree([3, 9, 20, None, None, 15, 7])))  # [3.0, 14.5, 11.0]

    # Test 2: root = [3,9,20,15,7] → [3.0, 14.5, 11.0]
    print(sol.averageOfLevels(make_tree([3, 9, 20, 15, 7])))  # [3.0, 14.5, 11.0]

    # Test 3: root = [1] → [1.0]
    print(sol.averageOfLevels(make_tree([1])))  # [1.0]