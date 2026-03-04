from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_h = self._height(root, go_left=True)
        right_h = self._height(root, go_left=False)
        # 왼쪽 == 오른쪽이면 포화 이진 트리
        if left_h == right_h:
            return (1 << left_h) - 1
        # 아니면 좌우 서브트리로 재귀
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def _height(self, root, go_left):
        height = 0
        while root:
            height += 1
            root = root.left if go_left else root.right
        return height


if __name__ == "__main__":
    sol = Solution()

    # Test 1: [1,2,3,4,5,6] → 6
    #       1
    #      / \
    #     2   3
    #    / \ /
    #   4  5 6
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    print(sol.countNodes(root1))  # Expected: 6

    # Test 2: [] → 0
    print(sol.countNodes(None))   # Expected: 0

    # Test 3: [1] → 1
    print(sol.countNodes(TreeNode(1)))  # Expected: 1
