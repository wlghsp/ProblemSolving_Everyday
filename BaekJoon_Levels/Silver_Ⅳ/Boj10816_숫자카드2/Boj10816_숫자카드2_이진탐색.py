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

def binary_search(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if arr[mid] == target:
        return count.get(target)
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return binary_search(arr, target, start, mid - 1)

for target in candidate:
    print(binary_search(cards, target, 0, len(cards) -1), end=" ")