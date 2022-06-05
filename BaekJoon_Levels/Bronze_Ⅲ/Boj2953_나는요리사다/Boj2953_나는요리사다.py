
import sys
input = lambda : sys.stdin.readline().rstrip()


human = [list(map(int, input().split())) for _ in range(5)]
# 각 참가자의 총합 점수 저장 변수
humanScore = [0] * 5
# 최대점수 저장 변수
score = 0

for i in range(5):
    sum = 0
    for j in range(4):
        sum += human[i][j]
    humanScore[i] = sum
    score = max(score, sum)

for i in range(5):
    if humanScore[i] == score:
        print(i+1, score)
        break