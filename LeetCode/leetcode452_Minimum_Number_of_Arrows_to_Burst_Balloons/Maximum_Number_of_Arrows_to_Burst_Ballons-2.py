from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 가장 빨리 끝나는 풍선부터 처리하고자 끝점 정렬하며
        #
        points.sort(key=lambda x: x[1])
        arrow_pos = points[0][1]
        arrows = 1

        for i in range(1, len(points)):
            # 현재 구간 시작점이 화살 위치보다 크면, 새 화살 필요
            if points[i][0] > arrow_pos:
                arrows += 1
                arrow_pos = points[i][1]

        return arrows

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])) # 2
