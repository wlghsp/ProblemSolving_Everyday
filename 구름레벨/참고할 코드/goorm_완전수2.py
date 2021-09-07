import sys
import math

input = lambda: sys.stdin.readline().rstrip()


def isPerfectNumber(n):
    divisors = [
        1,
    ]  # 1은 항상 약수이므로 미리 포함 및 1이 들어 있어 본인이 제외됨
    # 소수판별 시에도 이와 같이 알고리즘 개선 가능
    for i in range(2, int(math.sqrt(n)) + 1):  # 본인의 제곱근까지만 계산하면 나머지 약수는 아래와 같이 구한다.
        if n % i == 0:
            divisors.append(i)  # i가 약수
            divisors.append(n / i)  # n/i도 약수
    return sum(divisors) == n


def main():
    perfectNumbers = []
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if i == 1:  # 1은 완전수에서 배제
            continue
        if isPerfectNumber(i):
            perfectNumbers.append(i)
    if perfectNumbers:
        print(*perfectNumbers, end=" ")


if __name__ == "__main__":
    main()
