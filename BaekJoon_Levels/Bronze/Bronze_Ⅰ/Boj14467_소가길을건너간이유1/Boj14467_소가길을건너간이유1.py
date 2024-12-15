import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

cows = dict()
cnt = 0
for _ in range(N):
    cow_num, loc = map(int, input().split())
    if cow_num not in cows:
        cows[cow_num] = loc
    elif cow_num in cows and loc != cows[cow_num]:
        cnt += 1
        cows[cow_num] = loc
print(cnt)