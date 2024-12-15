import sys
input = lambda : sys.stdin.readline().rstrip()



arr = sorted(list(map(int, input().split())))

print(arr[1])