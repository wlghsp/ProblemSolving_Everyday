from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1,0]])) # true
    print(sol.canFinish(2, [[1,0],[0,1]])) # false
