
import sys
input = lambda : sys.stdin.readline().rstrip()


# 최대공약수 구하기
def GCD(a, b):
    for i in range(min(a,b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def LCM(a, b):
    for i in range(max(a,b), (a*b)+ 1):
        if i % a == 0 and i % b == 0:
            return i

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(LCM(a, b), GCD(a, b))
