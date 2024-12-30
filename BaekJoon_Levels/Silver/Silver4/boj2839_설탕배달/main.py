import sys

input = lambda: sys.stdin.readline().rstrip()

def sugar_delivery(n):
    count = 0
    while n >= 0:
        if n % 5 == 0: # 5키로로 나누어 떨어지는 경우
            count += n // 5
            return count
        n -= 3 # 5키로으로 나누어떨어지지 않으면 3키로 봉지를 하나 추가
        count += 1
    return -1 # 정확히 나눌 수 없는 경우


N = int(input())
print(sugar_delivery(N))
