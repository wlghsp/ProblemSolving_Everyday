from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indgree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
            indgree[a] += 1

        q = deque()
        for i in range(numCourses):
            if indgree[i] == 0:
                q.append(i)
        result = []
        while q:
            node = q.popleft()
            result.append(node)

            for neighbor in graph[node]:
                indgree[neighbor] -= 1
                if indgree[neighbor] == 0:
                    q.append(neighbor)

        return True if len(result) == numCourses else False


if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1,0]])) # true
    print(sol.canFinish(2, [[1,0],[0,1]])) # false
