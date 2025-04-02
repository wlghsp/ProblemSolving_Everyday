from collections import defaultdict

T = int(input())

for _ in range(T):
    # 팀의 개수 n, 문제의 개수 k, 당신 팀의 ID t, 로그 엔트리의 갯수 m
    n, k, t, m = map(int, input().split())
    logs = [list(map(int, input().split())) for _ in range(m)]
    scores = defaultdict(int)
    teams = {i: [0, 0, 0] for i in range(1, n + 1)}

    for i in range(m):
        team_id, prob_num, score = logs[i]
        prev = scores[(team_id, prob_num)]
        scores[(team_id, prob_num)] = max(prev, score)
        team = teams[team_id]
        team[1] += 1
        team[2] = i

    for team_id, prob_num in scores.keys():
        team = teams[team_id]
        team[0] += scores[(team_id, prob_num)]

    sorted_teams = sorted(teams.items(), key=lambda x: (-x[1][0], x[1][1], x[1][2]))
    rank = 1
    for a, _ in sorted_teams:
        if a == t:
            print(rank)
            break
        rank += 1
