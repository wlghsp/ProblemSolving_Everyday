# 중복이 없는 sorted list 안에 target이 존재한다면 그 index를 반환

def bs(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1


arr = [2, 5, 17, 22, 27, 35, 42, 51, 62, 70]
target = 51
print(bs(arr, target))