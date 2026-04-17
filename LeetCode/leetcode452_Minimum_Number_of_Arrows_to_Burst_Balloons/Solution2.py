from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrows = 1
        points.sort(key=lambda x: x[1])
        prev = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > prev:
                arrows += 1
                prev = points[i][1]

        return arrows


if __name__ == "__main__":
    s = Solution()

    # Example 1: Expected 2
    print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))

    # Example 2: Expected 4
    print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))

    # Example 3: Expected 2
    print(s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
