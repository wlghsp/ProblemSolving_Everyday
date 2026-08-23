"""
Level 1 - 순열 생성 기초

백트래킹으로 순열을 만드는 뼈대 감각을 익힙니다.
itertools.permutations 사용 금지 - 직접 재귀/백트래킹으로 구현하세요.

힌트가 필요하면 대화창에서 "힌트" 요청하세요 (Level 1 -> 2 -> 3 순서로 제공).
"""


def permute(nums: list[int]) -> list[list[int]]:
    # nums로 만들 수 있는 모든 순열을 리스트로 반환 (순서 상관 없음)
    # 예: nums=[1,2,3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] (순서 무관)
    ans = []
    n = len(nums)
    def backtrack(curr, visited):
        if len(curr) == n:
            ans.append(curr[:])
            return
        loop = set()
        for i in range(n):
            if visited[i]: continue
            if nums[i] in loop: continue

            loop.add(nums[i])
            curr.append(nums[i])
            visited[i] = True
            backtrack(curr, visited)
            visited[i] = False
            curr.pop()

    backtrack([], [False] * n)

    return ans


def permute_count(n: int) -> int:
    # n개의 서로 다른 원소로 만들 수 있는 순열의 총 개수를 반환 (n!)
    # 반복문 또는 재귀로 직접 계산 - math.factorial 사용 금지
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans


if __name__ == "__main__":
    result = permute([1, 2, 3])
    assert len(result) == 6
    assert sorted(result) == sorted([
        [1, 2, 3], [1, 3, 2],
        [2, 1, 3], [2, 3, 1],
        [3, 1, 2], [3, 2, 1],
    ])

    result_single = permute([5])
    assert result_single == [[5]]

    assert permute_count(0) == 1
    assert permute_count(1) == 1
    assert permute_count(3) == 6
    assert permute_count(5) == 120

    print("Level 1 all tests passed!")
