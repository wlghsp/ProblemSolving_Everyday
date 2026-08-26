"""
Level 4 - 도달 불가능한 상태를 안전하게 다루기 (INF 패턴)

지금까지는 모든 상태가 항상 "도달 가능"했습니다.
이 문제는 특정 조건(연속 두 칸 점프 금지) 때문에 일부 상태가
"애초에 도달할 수 없는" 경우가 생깁니다.

이런 상태를 0이나 임의의 값으로 두면, min()/max() 비교에서
"불가능한 경로"가 마치 "가능한 경로"처럼 섞여 들어가 답이 틀립니다.
그래서 도달 불가능한 상태는 min 문제에서는 +INF, max 문제에서는 -INF로
표현해서, 비교 연산에서 항상 지도록 만들어야 합니다.
"""


def min_cost_no_double_jump(cost: list[int]) -> int:
    # cost[i] = i번 계단을 밟을 때 드는 비용 (0-indexed).
    # 0번 계단에서 시작해서 마지막 계단(len(cost)-1)까지 이동합니다.
    # 한 번에 1칸 또는 2칸 이동 가능하지만, 2칸 점프를 연속으로 두 번 할 수 없습니다.
    # (즉 방금 2칸으로 착지했다면, 다음은 반드시 1칸만 가능)
    # 밟는 계단들의 cost 합의 최솟값을 반환하세요 (0번 계단의 cost도 포함).
    #
    # 힌트: dp[i][0] = i에 "1칸 점프로 착지"한 상태의 최소 비용
    #      dp[i][1] = i에 "2칸 점프로 착지"한 상태의 최소 비용
    # dp[i][1]로 오려면 직전(i-2)이 "2칸 점프로 착지"한 상태여서는 안 됩니다.
    # 그 전이가 불가능하면 그 상태는 INF로 두세요 (float('inf')).
    #
    # 예: cost=[1,2,3] -> 1번(0->1, 1칸) -> 2번(1->2, 1칸): 1+2+3=6
    #     또는 0->2 (2칸, cost 1+3=4)가 더 쌈
    # 예: cost=[5] -> 5 (계단이 1개뿐이면 그냥 거기 서 있음)
    INF = float('inf')
    n = len(cost)
    if n == 1:
        return cost[0]
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = cost[0]
    dp[0][1] = INF
    dp[1][0] = min(dp[0][0], dp[0][1]) + cost[1]
    dp[1][1] = INF

    for i in range(2, n):
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i]
        dp[i][1] = dp[i - 2][0] + cost[i]
    return min(dp[n - 1][0], dp[n - 1][1])


if __name__ == "__main__":
    assert min_cost_no_double_jump([5]) == 5
    assert min_cost_no_double_jump([1, 2, 3]) == 4
    assert min_cost_no_double_jump([1, 2, 3, 4, 5]) == 11
    assert min_cost_no_double_jump([4, 2, 7, 1, 3]) == 10

    print("Level 4 all tests passed!")
