"""
int는 32비트, long long 은 64비트라서 이 보다 더 큰 숫자는 저장할 수 없다.

아주 큰 숫자의 덧셈을 하려고 한다.

계산 결과를 출력하시오.

입력

첫째줄과 둘째줄에 큰 수 a, b가 입력된다. (a, b는 100자리 이하의 정수)

출력

큰 수 덧셈의 결과를 출력한다.

입력 예시

12345678910111213
2839287
출력 예시

12345678912950500



"""

import sys
input = lambda : sys.stdin.readline().rstrip()


a = int(input())
b = int(input())

print(a+b)