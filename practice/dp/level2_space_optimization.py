"""
Level 2 - 공간 최적화 (배열 -> 변수 롤링)

Level 1에서 만든 dp 배열을 보면, dp[i]를 구할 때 dp[i-1]과 dp[i-2]만 필요합니다.
그 이전 값들은 한 번 쓰이고 나면 다시 참조되지 않습니다.
즉, 배열 전체를 들고 있을 필요 없이 "최근 두 값"만 변수로 굴리면 됩니다.

이 문제들은 Level 1과 결과가 완전히 같아야 하지만, dp 배열(리스트)을 쓰면 안 됩니다.
"""


def climb_ways_optimized(n: int) -> int:
    # Level 1의 climb_ways와 동일한 결과를 반환하되,
    # dp = [0] * (n+1) 같은 배열을 사용하지 않고 변수 몇 개로만 구현하세요.
    if n <= 3:
        return n
    prev_prev = 1
    prev = 2
    for _ in range(3, n + 1):
        curr = prev + prev_prev
        prev_prev = prev
        prev = curr
    return curr


def min_cost_climb_optimized(cost: list[int]) -> int:
    # Level 1의 min_cost_climb과 동일한 결과를 반환하되,
    # 배열 없이 변수 몇 개로만 구현하세요.
    n = len(cost)
    if n < 2:
        return 0
    prev_prev = 0
    prev = 0
    for i in range(2, n + 1):
        curr = min(prev + cost[i - 1], prev_prev + cost[i - 2])
        prev_prev = prev
        prev = curr
    return prev


if __name__ == "__main__":
    assert climb_ways_optimized(2) == 2
    assert climb_ways_optimized(3) == 3
    assert climb_ways_optimized(4) == 5
    assert climb_ways_optimized(1) == 1

    assert min_cost_climb_optimized([10, 15, 20]) == 15
    assert min_cost_climb_optimized([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert min_cost_climb_optimized([5]) == 0

    print("Level 2 all tests passed!")
