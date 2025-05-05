from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        if len(res) != numCourses:
            return []
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.findOrder(2, [[1,0]])) # [0,1]
    print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])) # [0,2,1,3]
    print(sol.findOrder(1, [])) # [0]