import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))
cnt = 1
maxVal = arr[-1]
for i in range(len(arr)-1, -1, -1):
    if arr[i] > maxVal:
        maxVal = arr[i]
        cnt += 1

print(cnt)