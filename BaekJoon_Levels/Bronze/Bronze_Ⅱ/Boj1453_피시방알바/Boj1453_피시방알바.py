import sys
input = lambda : sys.stdin.readline().rstrip()
people = []
n = int(input())
arr = list(map(int, input().split()))

set_arr = set(arr)
print(len(arr) - len(set_arr))

