import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
cards = sorted([*map(int, input().split())])
M = int(input())
candidate = [*map(int, input().split())]
count = {}

# 딕셔너리 이용, 키 조회
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for c in candidate:
    result = count.get(c)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")