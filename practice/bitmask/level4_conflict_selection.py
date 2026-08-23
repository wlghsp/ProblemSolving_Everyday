"""
Level 4 - 제약(conflict)이 있는 부분집합 선택

Level 3의 "전체 부분집합 순회"에 유효성 검사를 추가합니다.
이건 study/challenge-algorithm-thinking 레포의
week-03__internal-review-contrast 문제와 같은 유형입니다.

scores[i] = i번째 항목의 점수
conflicts = [[a, b], ...] : a와 b는 동시에 선택할 수 없음
k = 정확히 몇 개를 선택해야 하는지

k개를 선택하되 conflict 쌍을 피하면서 점수 합을 최대화하세요.
"""


def max_score_selection(scores: list[int], conflicts: list[list[int]], k: int) -> int:
    # 힌트: conflict_mask[i] = i와 충돌하는 원소들을 비트마스크로 미리 만들어두면
    # 특정 mask가 유효한지 O(n) 혹은 그 이하로 검사할 수 있습니다.
    pass


if __name__ == "__main__":
    # study/challenge-algorithm-thinking 레포의 공개 예제와 동일
    result = max_score_selection([8, 6, 7, 5, 9], [[0, 1], [1, 2], [3, 4]], 3)
    assert result == 24, f"got {result}"

    # conflict 없는 경우: 그냥 가장 큰 k개 합
    result2 = max_score_selection([1, 2, 3, 4], [], 2)
    assert result2 == 7  # 3 + 4

    print("Level 4 all tests passed!")
