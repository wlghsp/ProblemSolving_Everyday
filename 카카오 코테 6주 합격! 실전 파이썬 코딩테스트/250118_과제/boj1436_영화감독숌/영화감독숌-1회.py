N = int(input())

def is_doom(n):
    cnt = 0

    while n != 0:
        num = n % 10
        if num == 6:
            cnt += 1
        else: cnt = 0

        if cnt == 3:
            return True

        n = n // 10

    return False

n_doom = 0
number = 1
while True:
    if is_doom(number):
        n_doom += 1
    if n_doom == N:
        print(number)
        break

    number += 1