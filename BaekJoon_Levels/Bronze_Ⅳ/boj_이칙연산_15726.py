"""
32 16 8

64

한번 곱셈 한번 나눗셈 기호 

"""
import sys

input = lambda: sys.stdin.readline().rstrip()
a, b, c = map(int, input().split())
# 세 수의 순서는 변하지 않는다는 점을 못 보고 정렬로 계산하였기에 틀렸음.


# 블로그 참조함..
print(a * max(b, c) // min(b, c))

# 블로그 두 번째 참조
print(max(int(a*b/c), int(a/b*c)))