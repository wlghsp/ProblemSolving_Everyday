
N = int(input())
number_cards = set(list(map(int, input().split())))
M = int(input())
arr = list(map(int, input().split()))

for num in arr:
    print(1 if num in number_cards else 0, end=' ')
