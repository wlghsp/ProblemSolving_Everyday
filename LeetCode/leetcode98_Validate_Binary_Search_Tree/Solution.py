class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val # 현재 노드의 값
        self.left = left # 왼쪽 자식 노드
        self.right = right # 오른쪽 자식 노드
from typing import Optional


class Solution:
    """
    # 1. 범위 추적
    핵심 아이디어:
        - 각 노드는 허용 가능한 값의 범위를 가짐
        - 왼쪽으로 가면 -> 상한 max(업데이트)
        - 오른쪽으로 가면 -> 하한 min(업데이트
    """

    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            # 빈 노드는 유효
            if not node:
                return True

            # 현재 노드가 범위를 벗어나면 False
            if node.val <= min_val or node.val >= max_val:
                return False

            # 왼쪽: 상한을 현재 값으로 제한
            # 오른쪽: 하한을 현재 값으로 제한
            return (validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val))

        # 초기 범위: (-무한대, +무한대)
        return validate(root, float('-inf'), float('inf'))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        def inorder(node):
            if not node:
               return True

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
        inorder(root)

        for i in range(1, len(values)):
            if values[i - 1] >= values[i]:
                return False

        return True


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
    while queue and i < len(values):
        # 큐에서 노드 하나 꺼내기
        node = queue.pop(0)

        # 4. 왼쪽 자식 처리
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left) # 큐에 추가
        i += 1

        # 5. 오른쪽 자식 처리
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right) # 큐에 추가
        i += 1
    return root

if __name__ == "__main__":
    sol = Solution()
    root1 = build_tree([2, 1, 3])
    print(f"예시 1: {sol.isValidBST(root1)}")  # Expected: True
    root2 = build_tree([5, 1, 4, None, None, 3, 6])
    print(f"예시 2: {sol.isValidBST(root2)}")  # Expected: False (3 < 5)

