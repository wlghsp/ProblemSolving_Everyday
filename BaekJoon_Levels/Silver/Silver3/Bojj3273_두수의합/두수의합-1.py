N = int(input())
arr = list(map(int, input().split()))
X = int(input())
arr.sort()
left, right = 0, len(arr) - 1

result = 0
while left < right:
    num = arr[left] + arr[right]
    if num == X:
        result += 1
        left += 1
        right -= 1
    elif num > X:
        right -= 1
    elif num < X:
        left += 1

print(result)