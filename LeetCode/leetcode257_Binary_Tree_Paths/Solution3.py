from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def dfs(node, path):
            path += str(node.val)
            if node and not node.left and not node.right:
                result.append(path)
                return
            if node.left:
                dfs(node.left, path + "->")
            if node.right:
                dfs(node.right, path + "->")
        dfs(root, "")
        return result


if __name__ == "__main__":
    s = Solution()

    # Example 1:
    #     1
    #    / \
    #   2   3
    #    \
    #     5
    # Expected: ["1->2->5", "1->3"]
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
    print(s.binaryTreePaths(root))

    # Example 2: single node
    # Expected: ["1"]
    print(s.binaryTreePaths(TreeNode(1)))
