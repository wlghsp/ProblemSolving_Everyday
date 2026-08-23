"""
Level 5 - dp[mask] 형태의 비트마스크 DP

LeetCode 1125. Smallest Sufficient Team 과 유사한 난이도의
"커버리지" 문제입니다.

people[i] = i번째 사람이 커버할 수 있는 스킬들을 나타내는 인덱스 리스트
skills = 전체 스킬 목록 (예: ["java", "python", "sql"])

전체 스킬을 모두 커버하는 최소 인원 수를 구하세요.
(dp[mask] = mask가 나타내는 스킬 집합을 커버하는 데 필요한 최소 인원 수)
"""


def min_team_size(skills: list[str], people: list[list[str]]) -> int:
    # 힌트:
    # 1) skill_to_bit: 스킬 이름 -> 비트 인덱스 매핑
    # 2) person_mask[i]: i번째 사람이 커버하는 스킬을 비트마스크로 표현
    # 3) dp[mask] = mask를 커버하는 데 필요한 최소 인원 수, dp[0] = 0
    #    dp[mask | person_mask[i]] = min(dp[mask] + 1, ...) 로 전이
    # 4) 목표: dp[(1 << len(skills)) - 1]
    pass


if __name__ == "__main__":
    skills = ["java", "python", "sql"]
    people = [
        ["java"],
        ["python", "sql"],
        ["java", "python"],
    ]
    # 사람 0(java) + 사람 1(python, sql) = 2명으로 전체 커버 가능
    assert min_team_size(skills, people) == 2

    skills2 = ["a", "b", "c", "d"]
    people2 = [
        ["a", "b"],
        ["c", "d"],
        ["a", "b", "c", "d"],
    ]
    # 사람 2 혼자서 다 커버
    assert min_team_size(skills2, people2) == 1

    print("Level 5 all tests passed!")
