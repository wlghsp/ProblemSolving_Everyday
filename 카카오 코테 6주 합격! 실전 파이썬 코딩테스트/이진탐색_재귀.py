# 중복이 없는 sorted list 안에 target이 존재한다면 그 index를 반환

def bs_recur(arr, target, l, r):
    if l > r:
        return -1 # 종료 조건

    mid = l + (r - l) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return bs_recur(arr, target, l, mid - 1)
    else:
        return bs_recur(arr, target, mid + 1, r)



arr = [2, 5, 17, 22, 27, 35, 42, 51, 62, 70]
target = 51
print(bs_recur(arr, target, 0, len(arr) - 1))