from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0]) 
        mid = inorder.index(preorder[0]) 

        root.left = self.buildTree(preorder[1:], inorder[:mid]) # 왼쪽 서브트리
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:]) # 오른쪽 서브트리
        
        return root

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
