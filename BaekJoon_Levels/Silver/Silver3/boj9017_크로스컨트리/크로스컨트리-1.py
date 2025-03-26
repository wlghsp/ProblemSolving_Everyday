from collections import defaultdict

T = int(input())

for _ in range(T):
    N = int(input())
    INF = float('inf')
    players = list(map(int, input().split()))

    # 팀 선수 기록 딕셔너리
    team_counts = defaultdict(int)
    # 팀 점수 기록 딕셔너리
    team_scores = defaultdict(list)

    # 선수 수 카운트
    for p in players:
        team_counts[p] += 1

    # 스코어 기록
    score = 1
    for p in players:
        if team_counts[p] == 6:
            team_scores[p].append(score)
            score += 1

    result = []
    for team, score in team_scores.items():
        # 점수 4명 합, 5번째 선수 점수, 팀 번호
        result.append((sum(score[:4]), score[4], team))
    # 정렬
    result.sort()

    print(result[0][2])
