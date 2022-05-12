
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

arr = [i for i in map(int, input().split())]
arr.sort()

prev = 0
sum = 0

for i in range(N):
    sum += prev + arr[i];

    prev += arr[i];

print(sum)