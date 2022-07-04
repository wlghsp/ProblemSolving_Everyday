import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

arr = [False] * 2000001

for i in range(N):
    arr[1000000 + int(input())] = True


for i in range(len(arr)-1, -1, -1):
    if arr[i]:
        print(i - 1000000)
