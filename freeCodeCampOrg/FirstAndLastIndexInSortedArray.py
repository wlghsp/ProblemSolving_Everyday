# def first_and_last(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             start = i
#             while i + 1 < len(arr) and arr[i + 1] == target:
#                 i += 1
#             return [start, i]
#     return [-1, -1]

# def first_and_last(arr, target):
#     if len(arr) == 0:
#         return [-1, -1]
#     start = find_start(arr, target)
#     if start == -1:
#         return [-1, -1]
#     end = start
#     while end + 1 < len(arr) and arr[end + 1] == target:
#         end += 1
#     return [start, end]





def find_end(arr, target):
    if arr[-1] == target:
        return len(arr) -1
    left, right = 0, len(arr) -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid + 1] > target:
            return mid
        elif arr[mid] > target:
            right = mid + 1
        else:
            left = mid + 1
    return -1

def find_start(arr, target):
    if arr[0] == target:
        return 0
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid - 1] < target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def first_and_last(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]
    start = find_start(arr, target)
    end = find_end(arr, target)
    return [start, end]


arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
target = 5

print(first_and_last(arr, target))

# output [2,6]
