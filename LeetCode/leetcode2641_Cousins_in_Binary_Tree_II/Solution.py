from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree(lst, i=0):
    if i >= len(lst) or lst[i] is None:
        return None
    node = TreeNode(lst[i])
    node.left = make_tree(lst, 2*i+1)
    node.right = make_tree(lst, 2*i+2)
    return node

def print_tree(root):
    if not root:
        return []
    result, q = [], deque([root])
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return result

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([(None, root)])

        while q:
            levels = []
            nodes = {}
            parents = set()
            level_sum = 0
            for _ in range(len(q)):
                parent, node = q.popleft()

                nodes[parent] = nodes.get(parent, 0) + node.val
                level_sum += node.val
                levels.append((parent, node))
                parents.add(parent)

                if node.left:
                    q.append((node, node.left))
                if node.right:
                    q.append((node, node.right))

            for parent, node in levels:
                node.val = level_sum - nodes[parent]

        return root
    
if __name__ == "__main__":
    sol = Solution()

    # Test 1: root = [5,4,9,1,10,null,7] → [0,0,0,7,7,null,11]
    # 각 노드를 같은 레벨의 사촌들 합으로 교체
    result = sol.replaceValueInTree(make_tree([5, 4, 9, 1, 10, None, 7]))
    print(print_tree(result))  # [0, 0, 0, 7, 7, 11]

    # Test 2: root = [3,1,2] → [0,0,0]
    result = sol.replaceValueInTree(make_tree([3, 1, 2]))
    print(print_tree(result))  # [0, 0, 0]
