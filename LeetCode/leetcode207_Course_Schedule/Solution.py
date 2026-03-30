from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0] * numCourses

        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        result = []
        while q:
            node = q.popleft()
            result.append(node)

            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
                

        return True if len(result) == numCourses else False


if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    numCourses = 2
    prerequisites = [[1, 0]]
    print(f"Test 1: {sol.canFinish(numCourses, prerequisites)}")  # Expected: True

    # Test case 2
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(f"Test 2: {sol.canFinish(numCourses, prerequisites)}")  # Expected: False

    # Test case 3
    numCourses = 1
    prerequisites = []
    print(f"Test 3: {sol.canFinish(numCourses, prerequisites)}")  # Expected: True

    # Test case 4
    numCourses = 3
    prerequisites = [[1, 0], [2, 1]]
    print(f"Test 4: {sol.canFinish(numCourses, prerequisites)}")  # Expected: True

    # Test case 5
    numCourses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2], [0, 3]]
    print(f"Test 5: {sol.canFinish(numCourses, prerequisites)}")  # Expected: False (cycle)
