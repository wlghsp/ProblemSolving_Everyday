from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.oldToNew = {}        
        return self.dfs(node)
    def dfs(self, node):
        if not node:
            return None
        if node in self.oldToNew:
            return self.oldToNew[node]

        copy = Node(node.val)
        self.oldToNew[node] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(self.dfs(neighbor))
        return copy

if __name__ == "__main__":
    sol = Solution()

    # Test 1: [[2,4],[1,3],[2,4],[1,3]]
    # 1 - 2
    # |   |
    # 4 - 3
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    cloned = sol.cloneGraph(n1)
    if cloned:
        print(cloned.val)                          # 1
        print([n.val for n in cloned.neighbors])   # [2, 4]

    # Test 2: 노드 1개, 이웃 없음
    single = Node(1)
    cloned2 = sol.cloneGraph(single)
    if cloned2:
        print(cloned2.val)        # 1
        print(cloned2.neighbors)  # []

    # Test 3: None
    print(sol.cloneGraph(None))   # None
