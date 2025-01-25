
N = int(input())

def is_hansu(number):
    if number < 100:
        return True

    hun = number // 100
    ten = number // 10 % 10
    one = number % 10

    return True if (hun - ten) == (ten - one) else False
cnt = 0
for i in range(1, N + 1):
    if is_hansu(i):
        cnt += 1
print(cnt)
