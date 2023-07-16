import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

hint = [list(map(int, input().split())) for _ in range(4)]

answer = 0

for a in range(1, 10):
    for b in range(1,10):
        for c in range(1, 10):

            if (a == b or b == c or c == a):
                continue

            # 숫자가 정해졌다면

            for arr in hint:
                number, ball, strike = arr[0], arr[1], arr[2]

                # a, b, c 라는 숫자를
                # number하고 비교해서
                ball_count = 0
                strike_count = 0

                if ball == ball_count and strike == strike_count:
                    cnt = cnt + 1
            if cnt == n:
                answer = answer + 1

print(answer)