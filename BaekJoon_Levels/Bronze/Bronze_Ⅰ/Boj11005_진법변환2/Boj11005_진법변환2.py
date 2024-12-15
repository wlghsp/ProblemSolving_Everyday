import sys

input = lambda: sys.stdin.readline().rstrip()


# 10진법 수 N을 B진법으로 바꿔 출력
N, B = map(int, input().split())
tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

answer = ''

while N != 0:
    answer += str(tmp[N % B])
    N //= B

print(answer[::-1])
