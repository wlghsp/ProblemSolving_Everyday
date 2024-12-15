import sys
input = lambda : sys.stdin.readline().rstrip()

# B진법 수 N을 10진법 수로 바꿔 출력
N, B = input().split()

N = N[::-1]

B = int(B)

number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0

for x in range(len(N)):
    result += number.index(N[x]) * (B**x)

print(result)