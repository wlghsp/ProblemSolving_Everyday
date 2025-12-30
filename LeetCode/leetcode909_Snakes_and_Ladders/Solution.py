from typing import List
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        LeetCode 909. Snakes and Ladders

        뱀과 사다리 게임판이 주어질 때, 1번 칸에서 시작해서 n^2번 칸에 도달하는 최소 이동 횟수를 구하기
        도달할 수 없으면 -1 반환

        시간복잡도: O(n^2) - 각 칸을 최대 한 번씩 방문
        공간복잡도: O(n^2) - 큐와 방문 체크 배열
        """
        pass


# 테스트 케이스
if __name__ == "__main__":
    solution = Solution()

    # 테스트 1
    print("테스트 1:")
    board1 = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]
    result1 = solution.snakesAndLadders(board1)
    print(f"결과: {result1}")
    print(f"예상: 4")
    print("설명: 1→2→15(사다리)→17→36(목적지)\n")

    # 테스트 2
    print("테스트 2:")
    board2 = [
        [-1, -1],
        [-1, 3]
    ]
    result2 = solution.snakesAndLadders(board2)
    print(f"결과: {result2}")
    print(f"예상: 1")
    print("설명: 1→4(사다리로 한 번에)\n")

    # 테스트 3
    print("테스트 3:")
    board3 = [
        [-1, -1, -1],
        [-1, 9, 8],
        [-1, 8, 9]
    ]
    result3 = solution.snakesAndLadders(board3)
    print(f"결과: {result3}")
    print(f"예상: 1")
    print("설명: 1→9(사다리로 한 번에 목적지)\n")

    # 테스트 4: 큰 보드
    print("테스트 4:")
    board4 = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1]
    ]
    result4 = solution.snakesAndLadders(board4)
    print(f"결과: {result4}")
    print(f"예상: 5")
    print("설명: 뱀/사다리 없이 최대 6칸씩 이동\n")

    # 테스트 5: 뱀으로 뒤로 가는 케이스
    print("테스트 5:")
    board5 = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, 14, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1]
    ]
    result5 = solution.snakesAndLadders(board5)
    print(f"결과: {result5}")
    print(f"예상: 5\n")
