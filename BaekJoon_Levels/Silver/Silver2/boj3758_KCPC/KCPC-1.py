from collections import defaultdict

T = int(input())

for _ in range(T):
    # 팀의 개수 n, 문제의 개수 k, 당신 팀의 ID t, 로그 엔트리의 갯수 m
    n, k, t, m = map(int, input().split())
    logs = [list(map(int, input().split())) for _ in range(m)]
    best_scores = defaultdict(int)
    team_stats = {i: [0, 0, 0] for i in range(1, n + 1)}

    for i in range(m):
        team_id, prob_num, score = logs[i]
        key = (team_id, prob_num)
        best_scores[key] = max(best_scores[key], score)

        team_stats[team_id][1] += 1
        team_stats[team_id][2] = i

    for (team_id, prob_num), score in best_scores.items():
        team_stats[team_id][0] += score

    sorted_teams = sorted(team_stats.items(), key=lambda x: (-x[1][0], x[1][1], x[1][2]))

    for rank, (team_id, _) in enumerate(sorted_teams, start=1):
        if team_id == t:
            print(rank)
            break
