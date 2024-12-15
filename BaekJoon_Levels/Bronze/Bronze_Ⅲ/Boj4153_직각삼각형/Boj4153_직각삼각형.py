import sys

input = lambda: sys.stdin.readline().rstrip()

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0: break

    if (a * a + b * b) == (c * c): # c가 제일 긴 변인 경우
        print("right")
    elif (a * a + c * c) == (b * b): # b가 제일 긴 변인 경우
        print("right")
    elif (b * b + c * c) == (a * a): # c가 제일 긴 변인 경우
        print("right")
    else:
        print("wrong")
