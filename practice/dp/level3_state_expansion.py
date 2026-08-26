"""
Level 3 - 상태 확장 (마지막 행동을 상태에 포함)

Level 1~2의 dp[i]는 "i까지의 답"만 담았습니다.
이 문제는 "직전에 어떤 행동을 했는지"에 따라 다음 선택지가 달라지므로,
dp[i] 하나만으로는 다음 전이를 결정할 수 없습니다.

풀기 전에 먼저 답해보세요 (코드보다 이 설계가 먼저입니다):
- dp[i][0]과 dp[i][1]을 각각 어떤 의미로 정의할 것인가?
- 그 정의 위에서 전이식은 어떻게 되는가?
"""


def max_non_adjacent_sum(nums: list[int]) -> int:
    # nums에서 인접하지 않은 원소들만 골라 합의 최댓값을 구하세요.
    # (LeetCode 198 House Robber와 동일한 유형)
    # 힌트: dp[i][0] = i번째를 "선택 안 함" 상태로 i까지 봤을 때 최대합
    #      dp[i][1] = i번째를 "선택함" 상태로 i까지 봤을 때 최대합
    # 예: nums=[2,7,9,3,1] -> 12 (2+9+1)
    # 예: nums=[5,1,1,5] -> 10 (5+5)
    n = len(nums)
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = nums[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = dp[i - 1][0] + nums[i]
    return max(dp[n - 1][0], dp[n - 1][1])


def max_non_adjacent_sum_1d(nums: list[int]) -> int:
    # max_non_adjacent_sum과 동일한 결과를 반환하되,
    # dp[i][0]/dp[i][1] 2차원 상태 없이, dp[i] = max(dp[i-1], dp[i-2] + nums[i]) 형태의
    # 1차원 점화식으로 구현하세요. (2D 상태를 압축해서 유도한 결과)
    n = len(nums)
    dp = [0] * n
    if n == 1:
        return nums[0]
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[n - 1]


if __name__ == "__main__":
    assert max_non_adjacent_sum([2, 7, 9, 3, 1]) == 12
    assert max_non_adjacent_sum([5, 1, 1, 5]) == 10
    assert max_non_adjacent_sum([5]) == 5
    assert max_non_adjacent_sum([3, 2]) == 3
    assert max_non_adjacent_sum([1, 2, 3, 1]) == 4

    assert max_non_adjacent_sum_1d([2, 7, 9, 3, 1]) == 12
    assert max_non_adjacent_sum_1d([5, 1, 1, 5]) == 10
    assert max_non_adjacent_sum_1d([5]) == 5
    assert max_non_adjacent_sum_1d([3, 2]) == 3
    assert max_non_adjacent_sum_1d([1, 2, 3, 1]) == 4

    print("Level 3 all tests passed!")
