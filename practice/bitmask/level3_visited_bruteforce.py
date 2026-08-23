"""
Level 3 - visited 배열을 비트마스크로 대체 (완전탐색)

LeetCode 78. Subsets 와 동일한 문제를 "비트마스크로 전체 부분집합을 순회"하는
방식으로 풉니다. 재귀 백트래킹이 아니라 for mask in range(1 << n) 방식으로 구현하세요.
"""


def subsets(nums: list[int]) -> list[list[int]]:
    # nums의 모든 부분집합을 반환 (순서 무관)
    # 힌트: mask 하나가 부분집합 하나. mask의 각 비트가 nums의 각 원소를 포함하는지 나타냄.
    pass


if __name__ == "__main__":
    result = subsets([1, 2, 3])
    result_as_sets = {tuple(sorted(s)) for s in result}

    expected = {
        (), (1,), (2,), (3,),
        (1, 2), (1, 3), (2, 3),
        (1, 2, 3),
    }

    assert result_as_sets == expected, f"got {result_as_sets}"
    assert len(result) == 8  # 2^3

    print("Level 3 all tests passed!")
