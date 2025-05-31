import sys

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
