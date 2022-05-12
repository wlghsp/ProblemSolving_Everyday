

"""
뒷자리가 0이 나오는 경우를 찾는다.
5를 곱하면 0의 개수를 구할 수 있다.
5! 은 1X2X3X4X5 = 120 인데 5가 1개가 있어 0이 1개 있다.

결론: 단순히 5로 나눌 것이 아니라 반복문을 통해 5로 나누면서 누적합
"""
import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())

# 0의 개수
cnt = 0


# N이 5이상이면 while문 돌려
while N >= 5:
    # 5로 나눈 몫은 0의 개수가 되고
    cnt += N // 5

    #
    N //= 5

print(cnt)