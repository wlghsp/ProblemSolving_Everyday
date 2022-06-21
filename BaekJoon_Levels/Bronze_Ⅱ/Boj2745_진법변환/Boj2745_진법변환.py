import sys
input = lambda : sys.stdin.readline().rstrip()


N, B = input().split()

N = ''.join(reversed(N))

B = int(B)

number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0

for x in range(len(N)-1, -1, -1):
    total = number.index(N[x]) * (B**x)
    result += total

print(result)