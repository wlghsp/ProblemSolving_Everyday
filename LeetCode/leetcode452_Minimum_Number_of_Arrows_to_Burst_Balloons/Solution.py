from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x : (x[1], x[0]))
        res, prev = 1, points[0][1]
        for start, end in points[1:]:
            if not (start <= prev <= end):
                res += 1
                prev = end
        return res


if __name__ == "__main__":
    s = Solution()

    # Example 1: Expected 2
    print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))

    # Example 2: Expected 4
    print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))

    # Example 3: Expected 2
    print(s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
