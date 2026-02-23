from typing import Optional

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.max_len = max(self.max_len, left + right)
            return max(left, right) + 1
        dfs(root)
        return self.max_len

if __name__ == "__main__":
    sol = Solution()

    # Test 1: [1,2,3,4,5] → 3 (경로: 4→2→1→3 또는 5→2→1→3)
    print(sol.diameterOfBinaryTree(make_tree([1,2,3,4,5])))  # 3

    # Test 2: [1,2] → 1
    print(sol.diameterOfBinaryTree(make_tree([1,2])))  # 1

    # Test 3: [1] → 0
    print(sol.diameterOfBinaryTree(make_tree([1])))  # 0
