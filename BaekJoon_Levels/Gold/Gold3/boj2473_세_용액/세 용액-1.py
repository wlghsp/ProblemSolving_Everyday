import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

first_liquid, second_liquid, third_liquid = 0, 0, 0
min_diff = float('inf')
for i in range(N - 2):
    left, right = i + 1, N - 1

    while left < right:
        mixed_val = arr[i] + arr[left] + arr[right]

        if abs(mixed_val) < min_diff:
            min_diff = abs(mixed_val)
            first_liquid, second_liquid, third_liquid = arr[i], arr[left], arr[right]

        if mixed_val > 0:
            right -= 1
        elif mixed_val < 0:
            left += 1
        else:
            break

print(first_liquid, second_liquid, third_liquid)