'''
10 3
13 15 34 23 45 65 33 11 26 42

143
'''
import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())

set_arr = set()
arr = list(map(int, input().split()))

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            set_arr.add(arr[i] + arr[j] + arr[k])

arr = sorted(list(set_arr), reverse=True)

if len(arr) >= K:
    print(arr[K - 1])
else:
    print(-1)
