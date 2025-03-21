from math import inf

def find_closest_zero_triple(n, nums):
    nums.sort()
    first, second, third = 0, 0, 0
    min_diff = inf
    for start in range(n - 2):
        left, right = start + 1, n - 1

        while left < right:
            mixed = nums[start] + nums[left] + nums[right]

            if abs(mixed) < min_diff:
                min_diff = abs(mixed)
                first, second, third = nums[start], nums[left], nums[right]

            if mixed > 0:
                right -= 1
            elif mixed < 0:
                left += 1
            else:
                break

    return first, second, third


N = int(input())
arr = list(map(int, input().split()))
a, b, c = find_closest_zero_triple(N, arr)
print(a, b, c)

