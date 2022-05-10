

N = int(input())
scores = list(map(int, input().split()))
answer, cnt = 0, 0

for i in range(len(scores)):
    if scores[i] == 1:
        cnt += 1
        answer += cnt
    else: cnt = 0

print(answer)
