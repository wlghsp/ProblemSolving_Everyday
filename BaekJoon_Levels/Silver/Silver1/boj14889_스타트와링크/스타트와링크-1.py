import sys

input = sys.stdin.readline
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

combs = []

def recur(picked, start, length):
    if len(picked) == length:
        if picked[0] == 1: # 절반만 보기 위해, 첫 번째 사람(1번)이 포함된 조합만 본다.
            combs.append(picked)
        return

    for i in range(start, N + 1):
        recur(picked + [i], i + 1, length)

recur([], 1, N / 2)
total = set([i for i in range(1, N + 1)])

def get_team_score(team):
    score = 0
    for i in range(len(team)):
        for j in range(i, len(team)):
            score += S[team[i] - 1][team[j] - 1] + S[team[j] - 1][team[i] - 1]
    return score

min_diff = float('inf')
for start in combs:
    link = total - set(start)
    diff = abs(get_team_score(start) - get_team_score(list(link)))
    min_diff = min(min_diff, diff)

print(min_diff)
