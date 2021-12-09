"""
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

4
1 3 5 7

3

"""
import sys

input = lambda: sys.stdin.readline().rstrip()


def isPrime(x):
    if x < 2:
        return False

    # for i in range(2, int(math.sqrt(x)) + 1):
    #     if x % i == 0:
    #         return False

    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1

    return True


n = int(input())

nums = list(map(int, input().split()))

cnt = 0
for n in nums:
    if isPrime(n):
        cnt += 1

print(cnt)
