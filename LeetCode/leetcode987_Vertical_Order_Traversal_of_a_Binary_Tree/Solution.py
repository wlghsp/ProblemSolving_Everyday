from typing import Optional, List
from collections import defaultdict

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

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1. DFS로 모든 노드 (col, row, val) 수집
        records = []
        def dfs(node, col, row):
            if not node:
                return
            records.append((col, row, node.val))
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)

        dfs(root, 0, 0)

        # 2. (col, row, val) 순으로 정렬
        records.sort()

        # 3. 같은 col끼리 묶어서 반환
        result = []
        cols = []
        col = records[0][0]
        for c, r, v in records:
            if col == c:
                cols.append(v)
            else:
                result.append(cols)
                col = c
                cols = [v]
                
        # 4. 마지막 값 처리
        result.append(cols)

        return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: root = [3,9,20,None,None,15,7] → [[9],[3,15],[20],[7]]
    print(sol.verticalTraversal(make_tree([3, 9, 20, None, None, 15, 7])))
    # Expected: [[9],[3,15],[20],[7]]

    # Test 2: root = [1,2,3,4,5,6,7] → [[4],[2],[1,5,6],[3],[7]]
    print(sol.verticalTraversal(make_tree([1, 2, 3, 4, 5, 6, 7])))
    # Expected: [[4],[2],[1,5,6],[3],[7]]

    # Test 3: root = [1,2,3,4,6,5,7] → [[4],[2],[1,5,6],[3],[7]]
    print(sol.verticalTraversal(make_tree([1, 2, 3, 4, 6, 5, 7])))
    # Expected: [[4],[2],[1,5,6],[3],[7]]
