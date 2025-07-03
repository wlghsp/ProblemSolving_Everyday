from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        # 왼쪽, 오른쪽 서브트리 flatten 먼저 처리
        self.flatten(root.left)
        self.flatten(root.right)

        # 왼쪽 트리를 오른쪽으로 옮기고
        temp_right = root.right
        root.right = root.left
        root.left = None

        # 오른쪽 끝으로 가서 원래 오른쪽 트리를 이어 붙어기
        curr = root
        while curr.right:
            curr = curr.right
        curr.right = temp_right


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    s.flatten(root)
    print(root) # [1,null,2,null,3,null,4,null,5,null,6]