from bisect import bisect_left
from itertools import product

N = input()# 이동하려고 하는 채널
length = len(N)
N = int(N)
M = int(input()) # 고장난 버튼의 개수
remote_buttons = [i for i in range(10)]
first_digits = [i for i in range(1, 10)]
if M > 0:
    broken_buttons = list(map(int, input().split())) # 고장난 버튼 번호
    for button in broken_buttons:
        remote_buttons.remove(button)
        if button != 0:
            first_digits.remove(button)

cur = 100 # 현재 채널 100번

def generate_comb_numbers(first_digits, remote_buttons, length):
    comb_numbers = []
    if len(remote_buttons) == 1:
        for i in range(1, length + 2):
            comb_numbers.append(int(str(remote_buttons[0]) * i))
        return comb_numbers
    else:
        for first in first_digits:
            for comb in product(remote_buttons, repeat= length - 1):
                num = int(str(first) + ''.join(map(str, comb)))
                comb_numbers.append(num)
    return comb_numbers


def find_closest(sorted_numbers, target):
    index = bisect_left(sorted_numbers, target)

    left_value = sorted_numbers[index - 1] if index > 0 else float('inf')
    right_value = sorted_numbers[index] if index < len(sorted_numbers) else float('inf')

    # 가장 가까운 값 반환
    if abs(target - left_value) <= abs(target - right_value):
        return left_value
    else:
        return right_value

comb_numbers = generate_comb_numbers(first_digits, remote_buttons, length)
sorted_numbers = sorted(comb_numbers)
closest_num = find_closest(sorted_numbers, N)

print(min(len(str(closest_num)) + abs(closest_num - N), abs(cur - N)))
