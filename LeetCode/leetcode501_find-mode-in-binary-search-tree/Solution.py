from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    501. Find Mode in Binary Search Tree

    BST에서 최빈값(가장 많이 등장하는 값)을 모두 반환하세요.
    최빈값이 여러 개면 모두 반환합니다.

    Constraints:
    - 노드 수: [1, 10^4]
    - -10^5 <= Node.val <= 10^5
    - BST (중복 값 허용)
    """

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        pass


def build_tree(values):
    """레벨 순서 리스트로 트리 생성 (None은 빈 노드)"""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    s = Solution()

    # Test case 1: [1, null, 2, 2] → [2]
    root1 = build_tree([1, None, 2, 2])
    print(s.findMode(root1))  # [2]

    # Test case 2: [0] → [0]
    root2 = build_tree([0])
    print(s.findMode(root2))  # [0]

    # Test case 3: [1, 1, 2] → [1]
    root3 = build_tree([1, 1, 2])
    print(s.findMode(root3))  # [1]
