# 병합정렬 코드

def custom_merge_sort(arr):
    if len(arr) <= 1: # 종료 조건
        return arr

    # 분할
    mid = len(arr) // 2
    left_half = custom_merge_sort(arr[:mid])
    right_half = custom_merge_sort(arr[mid:])
    # 병합
    return merge(left_half, right_half)

def merge(left, right): # 병합과정에서 정렬 이루어짐
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])  # 더 작은 쪽 먼저 append
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:] # 남아 있는 것 넣기
    result += right[j:]

    return result

