class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # low <= 노드값 <= high 범위에 있는 노드들의 합을 구하기
        if not root:
            return 0
        result = 0
        if root.val < low:
            result += self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            result += self.rangeSumBST(root.left, low, high)
        elif low <= root.val <= high:
            result += root.val
            result += self.rangeSumBST(root.left, low, high)
            result += self.rangeSumBST(root.right, low, high)
        return result


def build_tree(values):
    """Build tree from level-order list (None represents missing nodes)"""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


if __name__ == "__main__":
    sol = Solution()

    # Test 1: root = [10,5,15,3,7,null,18], low = 7, high = 15
    root1 = build_tree([10, 5, 15, 3, 7, None, 18])
    print(sol.rangeSumBST(root1, 7, 15))  # Expected: 32 (7+10+15)

    # Test 2: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
    root2 = build_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
    print(sol.rangeSumBST(root2, 6, 10))  # Expected: 23 (6+7+10)

    # Test 3: root = [10], low = 10, high = 10
    root3 = build_tree([10])
    print(sol.rangeSumBST(root3, 10, 10))  # Expected: 10
