
import sys
input = lambda : sys.stdin.readline().rstrip()


N = int(input())
arr = list(map(int, input().split()))

print(min(arr), end=' ')
print(max(arr))