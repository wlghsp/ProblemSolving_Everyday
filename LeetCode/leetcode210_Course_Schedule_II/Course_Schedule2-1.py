from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.findOrder(2, [[1,0]])) # [0,1]
    print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])) # [0,2,1,3]
    print(sol.findOrder(1, [])) # []