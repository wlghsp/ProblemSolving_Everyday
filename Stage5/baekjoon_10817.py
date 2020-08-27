# 20 30 10
# 20

# 30 30 10
# 30


import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
a.sort()
print(a[1])
