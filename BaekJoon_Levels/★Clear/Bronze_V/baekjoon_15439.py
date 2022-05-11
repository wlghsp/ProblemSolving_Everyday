import sys, itertools

input = sys.stdin.readline


num = int(input())

pairs = list(itertools.permutations(range(num), 2))
print(len(pairs))
