# 생성자가 있는 수들을 전부 찾고
# 전체에서 생성자가 없는 수를 제거하는
# 생성자: 생성자 있는 수를 제회한 수

N = int(input())

def is_hansu(number):
    if number < 100:
        return True

    hun = number // 100
    ten = number % 100 // 10
    one = number % 10

    return True if (hun - ten) == (ten - one) else False


hansu_nums = []
for i in range(1, N + 1):
    if is_hansu(i):
        hansu_nums.append(i)

print(len(hansu_nums))
