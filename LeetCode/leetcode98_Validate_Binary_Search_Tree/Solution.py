class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val # 현재 노드의 값
        self.left = left # 왼쪽 자식 노드
        self.right = right # 오른쪽 자식 노드
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pass


def build_tree(values):
    # 빈 리스트면 None 반환
    if not values:
        return None
    
    # 1. 루트 노드 생성
    root = TreeNode(values[0])

    # 2. 큐에 루트 추가 (BFS 방식)
    queue = [root]
    i = 1 # 다음 값의 인덱스

    # 3. 큐가 비거나 값을 다 쓸 때 까지
    while queu

if __name__ == "__main__":
    sol = Solution()
    root1 = build_tree([2, 1, 3])
    print(f"예시 1: {sol.isValidBST(root1)}")  # Expected: True
    root2 = build_tree([5, 1, 4, None, None, 3, 6])
    print(f"예시 2: {sol.isValidBST(root2)}")  # Expected: False (3 < 5)

