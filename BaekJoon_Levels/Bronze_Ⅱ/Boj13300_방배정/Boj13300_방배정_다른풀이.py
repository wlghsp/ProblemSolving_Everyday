import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

student = [[0, 0] for _ in range(6)] # 학년별로 남학생, 여학생 수

for _ in range(N):
    s, y = map(int, input().split())
    student[y-1][s] += 1

answer = 0
for grade in student:
    for sex in grade:
        answer += sex // K
        if sex % K:
            answer += 1

print(answer)
