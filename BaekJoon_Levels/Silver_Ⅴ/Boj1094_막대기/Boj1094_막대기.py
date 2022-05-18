

import sys

input = lambda : sys.stdin.readline().rstrip()

x = int(input()) # 64보다 작거나 같은 자연수

count = 0
stick = 64

while x > 0:
    # 스틱의 길이가 x보다 크면 절반으로 자르기
    if stick > x:
        stick /= 2
    # 스틱의 길이가 x보다 작으면 풀로 부텨
    else:
        count += 1
        x -= stick

print(count)