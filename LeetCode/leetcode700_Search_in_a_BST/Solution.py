class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        
        if root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)


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


def tree_to_list(root):
    """Convert tree to level-order list for easy comparison"""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: root = [4,2,7,1,3], val = 2
    root1 = build_tree([4, 2, 7, 1, 3])
    result1 = sol.searchBST(root1, 2)
    print(tree_to_list(result1))  # Expected: [2, 1, 3]

    # Test 2: root = [4,2,7,1,3], val = 5
    root2 = build_tree([4, 2, 7, 1, 3])
    result2 = sol.searchBST(root2, 5)
    print(tree_to_list(result2))  # Expected: []

    # Test 3: root = [1], val = 1
    root3 = build_tree([1])
    result3 = sol.searchBST(root3, 1)
    print(tree_to_list(result3))  # Expected: [1]
