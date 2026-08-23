"""
Level 1 - 기본 비트 연산

정수 n을 "비트 집합"으로 보고 아래 네 가지 기본 연산을 구현하세요.
i는 0부터 시작하는 비트 인덱스입니다 (0번 비트 = 최하위 비트).

힌트가 필요하면 대화창에서 "힌트" 요청하세요 (Level 1 -> 2 -> 3 순서로 제공).
"""


def is_set(n: int, i: int) -> bool:
    # i번째 비트가 켜져 있으면 True
    return (n & (1 << i)) != 0


def set_bit(n: int, i: int) -> int:
    # i번째 비트를 켠 새 정수를 반환 (n 자체는 변경하지 않음)
    return n | (1 << i)


def clear_bit(n: int, i: int) -> int:
    # i번째 비트를 끈 새 정수를 반환
    return n & ~(1 << i)


def toggle_bit(n: int, i: int) -> int:
    # i번째 비트를 뒤집은 새 정수를 반환
    return n ^ (1 << i)


if __name__ == "__main__":
    # n = 0b1010 (10)
    n = 0b1010

    assert is_set(n, 1) == True
    assert is_set(n, 0) == False

    assert set_bit(n, 0) == 0b1011
    assert set_bit(n, 1) == 0b1010  # 이미 켜져 있으면 그대로

    assert clear_bit(n, 1) == 0b1000
    assert clear_bit(n, 0) == 0b1010  # 이미 꺼져 있으면 그대로

    assert toggle_bit(n, 0) == 0b1011
    assert toggle_bit(n, 1) == 0b1000

    print("Level 1 all tests passed!")
