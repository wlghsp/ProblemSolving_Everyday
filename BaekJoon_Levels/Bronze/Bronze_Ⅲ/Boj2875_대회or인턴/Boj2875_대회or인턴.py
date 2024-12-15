import sys
input = lambda : sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
team = 0
# 여학생 2명, 남학생 1명 팀을 만들 수 있고,
# 인턴쉽도 보낼 수 있는 수인 동안 반복
while N >= 2 and M >=1 and N+M >= K+3:
    N -= 2
    M -= 1
    team += 1

print(team)