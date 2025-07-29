from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. 각 노드의 진입 차수를 저장할 배열(indegree) 생성
        indegree = [0] * numCourses
        # 2. 각 노드의 인접 리스트를 담을 그래프(graph) 생성
        graph = [[] for _ in range(numCourses)]

        # 3. prerequisites 배열을 순회하면서
        #  graph에 b -> a, 진입차수 배열에 진입차수 증가
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # 4. indegree가 0인 노드를 큐에 먼저 넣음 (시작 가능한 노드들)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        # 5. 큐를 BFS 방식으로 순회
        result = []
        while q:
            node = q.popleft()
            result.append(node)

            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        # 6. 모든 노드를 방문했는지 확인 result의 길이가 numCourses와 같으면 사이클이 없음 → 수강 가능
        return True if len(result) == numCourses else False


if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1,0]])) # true
    print(sol.canFinish(2, [[1,0],[0,1]])) # false
