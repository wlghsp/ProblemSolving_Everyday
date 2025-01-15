
N = int(input())
number_cards = set((map(int, input().split())))
M = int(input())
arr = list(map(int, input().split()))

result = [1 if a in number_cards else 0 for a in arr]
print(*result, sep=' ')