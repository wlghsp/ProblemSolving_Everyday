# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 둘다 None 이면 같은 트리
        if p is None and q is None:
            return True
        # 한쪽만 None 이면 다른 트리
        if p is None or q is None:
            return False
        # 두 노드의 값이 다르면? 다른 트리
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)