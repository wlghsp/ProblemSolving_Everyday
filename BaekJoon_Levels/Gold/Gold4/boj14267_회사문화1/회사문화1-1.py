import sys

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = {i: [] for i in range(N)}
