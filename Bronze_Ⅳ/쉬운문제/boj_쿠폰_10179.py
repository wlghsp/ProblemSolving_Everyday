"""
3
100.00
59.99
20.00

$80.00
$47.99
$16.00

20프로 할인해주는 쿠폰

쿠폰을 사용한 가격을 나타내시오. 

"""
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())  # 테스트케이스의 수
prices = []
for _ in range(n):
    prices.append(float(input()))

prices = list(map(lambda x: x * (4 / 5), prices))
for p in prices:
    print(f"${p:.2f}")
