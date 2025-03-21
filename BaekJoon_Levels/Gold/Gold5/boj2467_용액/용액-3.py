N = int(input())
arr = list(map(int, input().split()))

left, right = 0, len(arr) - 1
l_answer, r_answer = 0, 0
min_diff = float("inf")

while left < right:
    mixed = arr[left] + arr[right]

    if abs(mixed) < min_diff:
        min_diff = abs(mixed)
        l_answer, r_answer = arr[left], arr[right]

    if mixed > 0:
        right -= 1
    elif mixed < 0:
        left += 1
    else:
        break


print(l_answer, r_answer)