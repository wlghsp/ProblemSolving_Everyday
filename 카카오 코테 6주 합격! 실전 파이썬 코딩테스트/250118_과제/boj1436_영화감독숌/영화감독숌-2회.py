N = int(input())


def is_doom(number):
    count = 0
    while number != 0:
        num = number % 10
        if num == 6:
            count += 1
        else:
            count = 0

        if count >= 3:
            return True

        number //= 10

    return False


cnt = 0
start = 666
while True:
    if is_doom(start):
        cnt += 1
    if cnt == N:
        print(start)
        break
    start += 1
