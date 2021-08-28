"""
12 18

6

6 8

2

유클리드 호제법은 a, b, q, r이 정수라고 가정할 때
a = b * q + r =>  gcd(a, b) = gcd(b, a % b) 

숫자 a, b가 있을 때, a를 b로 나눈 나머지와 b 의 최대 공약수는 
a 와 b 의 최대 공약수 가 같다는 것을 의미한다.

그럼, 계속해서 a 를 b로 나누어서 b를 a에 나눈 나머지를 b 에 대입시켜서 b 가 0이 될때 까지 반복을
하면, 남는 a 값이 바로 최대 공약수 이다.

a와 b의 최대공약수는 b와 r의 최대공약수와 같다는 원리를 이용하여 최대공약수를 구한다. 
gcd( greatest common divisor) 최대공약수
lcm( least common multiple) 최소공배수
"""
import sys

input = lambda: sys.stdin.readline().rstrip()

# 흑흑 다 보고 적어버렸다. 잘 외우자. 유클리드 호제법 코드
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 최소공배수, a,b의 공통되는 배수 중에서 가장 작은 값
# a와 b의 곱을 , a,b의 최대 공약수로 나눈면 나옴.
def lcm(a, b):
    return a * b / gcd(a, b)


a, b = map(int, input().split())

print(gcd(a, b))
