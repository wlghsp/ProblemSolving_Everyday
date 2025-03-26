T = int(input())

for _ in range(T):
    N = int(input())
    INF = float('inf')
    players = list(map(int, input().split()))
    max_team_num = max(players)
    teams = {i: [0, [], INF] for i in range(1, max_team_num + 1)}
    for p in players:
        team = teams[p]
        team[0] += 1
    score = 1
    for p in players:
        team = teams[p]
        if team[0] == 6:
            team[1].append(score)
            score += 1
    result = [(0, 0, 0) for i in range(max_team_num + 1)]
    for k, v in teams.items():
        if v[0] == 6:
            sum_up_to_fourth = sum(v[1][:4])
            result[int(k)] = (sum_up_to_fourth, v[1][4], k)
    result = sorted(result)
    found = False
    ans = 0
    for a, b, c in result:
        if c != 0 and not found:
            ans = c
            found = True
    print(ans)