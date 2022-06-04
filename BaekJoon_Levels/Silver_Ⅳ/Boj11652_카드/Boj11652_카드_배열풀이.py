


import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))

cards.sort()
cnt, max = 1, 1
ans = cards[0]

for i in range(1, N):
    if cards[i] == cards[i-1]:
        cnt += 1
    else:
        cnt = 1

    if max < cnt:
        max = cnt
        ans = cards[i]

print(ans)