from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def dfs(pre_start, in_start, in_end):
            if  in_start > in_end:
                return None

            root = TreeNode(preorder[pre_start])
            mid = inorder_map[root.val]

            root.left = dfs(pre_start + 1, in_start, mid - 1)
            root.right = dfs(pre_start + (mid - in_start) + 1, mid + 1, in_end)

            return root
        return dfs(0, 0, len(inorder) - 1)

if __name__ == "__main__":
    def to_list(node):
        if not node: return []
        return [node.val] + to_list(node.left) + to_list(node.right)

    s = Solution()

    # preorder: [3,9,20,15,7], inorder: [9,3,15,20,7]
    # Expected tree: [3,9,20,null,null,15,7]
    root = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(to_list(root))  # [3, 9, 20, 15, 7]

    # preorder: [-1], inorder: [-1]
    root2 = s.buildTree([-1], [-1])
    print(to_list(root2))  # [-1]
