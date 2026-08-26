"""
Level 1 - 1D DP 기초 (계단 오르기)

가장 기본적인 선형 DP 감각을 익힙니다.
재귀 완전탐색이 아니라 DP(반복문 + 배열 또는 캐시)로 구현하세요.
"""


def climb_ways(n: int) -> int:
    # 계단이 n개 있고, 한 번에 1칸 또는 2칸을 오를 수 있다.
    # 지면(0번)에서 n번 계단까지 오르는 방법의 수를 반환.
    # 예: n=2 -> 2가지 (1+1, 2)
    # 예: n=4 -> 5가지 (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)
    pass


def min_cost_climb(cost: list[int]) -> int:
    # cost[i] = i번 계단을 밟을 때 드는 비용.
    # 0번 또는 1번 계단에서 시작해서, 한 번에 1칸 또는 2칸씩 올라
    # len(cost)번째(계단 밖, 도착점)까지 가는 최소 비용을 반환.
    # 예: cost=[10,15,20] -> 15 (1번에서 시작해 2칸 점프로 도착)
    pass


if __name__ == "__main__":
    assert climb_ways(2) == 2
    assert climb_ways(3) == 3
    assert climb_ways(4) == 5
    assert climb_ways(1) == 1

    assert min_cost_climb([10, 15, 20]) == 15
    assert min_cost_climb([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6

    print("Level 1 all tests passed!")
