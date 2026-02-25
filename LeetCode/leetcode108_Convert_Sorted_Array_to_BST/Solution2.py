from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_list(root):
    if not root:
        return []
    result, queue = [], deque([root])
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(lo, hi):
            if lo > hi:
                return
            mid = (lo + hi) // 2 
            root = TreeNode(nums[mid])
            root.left = helper(lo, mid - 1)
            root.right = helper(mid + 1, hi)
            return root
        return helper(0, len(nums) - 1)
        


if __name__ == "__main__":
    s = Solution()

    print(tree_to_list(s.sortedArrayToBST([-10, -3, 0, 5, 9])))  # [0, -3, 9, -10, None, 5] 등
    print(tree_to_list(s.sortedArrayToBST([1, 3])))               # [3, 1] 또는 [1, None, 3]
    print(tree_to_list(s.sortedArrayToBST([1])))                  # [1]
