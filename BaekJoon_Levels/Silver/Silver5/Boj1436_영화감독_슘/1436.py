

def is_doom1(n):
    cnt = 0
    while n != 0:
        num = n % 10

        if num == 6:
            cnt += 1
        else:
            cnt = 0

        if cnt == 3:
            return True

        n //= 10

    return False

def is_doom(n):
    return "666" in str(n)

N = int(input())


current_number = 1
doom_count = 0

while True:
    if is_doom(current_number):
        doom_count += 1

    if doom_count == N:
        print(current_number)
        break

    current_number += 1
