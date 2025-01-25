

N = int(input())

def is_doom(n):
    count = 0
    while n != 0:
        num = n % 10
        if num == 6:
            count += 1
        else: count = 0

        if count == 3:
            return True

        n //= 10

    return False

cnt = 0
number = 666
while True:
    if is_doom(number):
        cnt += 1
    if cnt == N:
        print(number)
        break

    number += 1