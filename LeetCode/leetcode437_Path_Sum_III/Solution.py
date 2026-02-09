from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pass


# Helper function for testing
def build_tree(values):
    """레벨 순서로 트리 생성"""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    root1 = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    result1 = solution.pathSum(root1, 8)
    print(f"Test 1: {result1}")  # Expected: 3

    # Test case 2
    root2 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    result2 = solution.pathSum(root2, 22)
    print(f"Test 2: {result2}")  # Expected: 3

    # Test case 3
    root3 = build_tree([1])
    result3 = solution.pathSum(root3, 1)
    print(f"Test 3: {result3}")  # Expected: 1
