class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root


if __name__ == "__main__":
    sol = Solution()

    def print_tree(node):
        if not node:
            return []
        result = []
        queue = [node]
        while queue:
            curr = queue.pop(0)
            if curr:
                result.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result

    # Test 1: [4,2,7,1,3,6,9] → [4,7,2,9,6,3,1]
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)
    print(print_tree(sol.invertTree(root1)))  # Expected: [4, 7, 2, 9, 6, 3, 1]

    # Test 2: [2,1,3] → [2,3,1]
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    print(print_tree(sol.invertTree(root2)))  # Expected: [2, 3, 1]
