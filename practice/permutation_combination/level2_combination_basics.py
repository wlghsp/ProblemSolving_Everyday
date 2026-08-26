"""
Level 2 - 조합(combination) 생성 기초

Level 1의 순열과 달리, 조합은 순서를 구분하지 않습니다.
itertools.combinations 사용 금지 - 직접 재귀/백트래킹으로 구현하세요.

힌트가 필요하면 대화창에서 "힌트" 요청하세요 (Level 1 -> 2 -> 3 순서로 제공).
"""


def combine(nums: list[int], k: int) -> list[list[int]]:
    # nums 중에서 k개를 뽑는 모든 조합을 리스트로 반환 (순서 상관 없음)
    # 예: nums=[1,2,3], k=2 -> [[1,2],[1,3],[2,3]] (순서 무관)
    ans = []
    n = len(nums)
    def comb(picked, start):
        if len(picked) == k:
            ans.append(picked[:])
            return
        for i in range(start, n):
            comb(picked + [nums[i]], i + 1)
        
    comb([], 0)
    
    return ans


def combine_count(n: int, k: int) -> int:
    # n개 중 k개를 뽑는 조합의 총 개수를 반환 (nCk)
    # 반복문 또는 재귀로 직접 계산 - math.comb 사용 금지
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    return combine_count(n - 1, k - 1) + combine_count(n - 1, k)


if __name__ == "__main__":
    result = combine([1, 2, 3], 2)
    assert sorted(result) == sorted([[1, 2], [1, 3], [2, 3]])

    result_full = combine([1, 2, 3], 3)
    assert result_full == [[1, 2, 3]]

    result_k0 = combine([1, 2, 3], 0)
    assert result_k0 == [[]]

    assert combine_count(5, 2) == 10
    assert combine_count(4, 0) == 1
    assert combine_count(4, 4) == 1
    assert combine_count(6, 3) == 20

    print("Level 2 all tests passed!")
