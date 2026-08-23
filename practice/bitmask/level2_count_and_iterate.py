"""
Level 2 - 비트 개수 세기 / 전체 부분집합 순회

Level 1의 is_set/set_bit 감각을 그대로 사용합니다.
"""


def count_bits(n: int) -> int:
    # n을 이진수로 표현했을 때 켜진 비트(1)의 개수를 반환
    # bin(n).count("1") 사용 금지 - 직접 비트 연산으로 구현
    count = 0
    while n > 0:
        n = n & (n - 1)
        count += 1
    return count


def list_subsets(n: int) -> list[int]:
    # n개의 원소가 있을 때, 가능한 모든 부분집합을 정수(마스크)로 표현해 리스트로 반환
    # 예: n=2 -> [0, 1, 2, 3] (원소 0개, {0}, {1}, {0,1})
    return list(range(1 << n))


def subset_to_indices(mask: int, n: int) -> list[int]:
    # mask가 나타내는 부분집합을 실제 인덱스 리스트로 변환
    # 예: mask=0b101, n=3 -> [0, 2]
    pass


if __name__ == "__main__":
    assert count_bits(0b1010) == 2
    assert count_bits(0) == 0
    assert count_bits(0b1111) == 4

    assert list_subsets(2) == [0, 1, 2, 3]
    assert len(list_subsets(5)) == 1 << 5

    assert subset_to_indices(0b101, 3) == [0, 2]
    assert subset_to_indices(0, 3) == []

    print("Level 2 all tests passed!")
