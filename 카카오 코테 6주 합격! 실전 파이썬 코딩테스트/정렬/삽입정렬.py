import random

test = random.sample(range(1, 10001), 20)
print(test)

# 삽입 정렬 코드
import bisect  # 이진 탐색 모듈


def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur = arr[i]  # 현재값
        pos = bisect.bisect_left(arr, cur, 0, i)  # 이진탐색을 사용하여 삽입할 위치 찾기
        arr = arr[:pos] + [cur] + arr[pos:i] + arr[i + 1:]  # 값을 해당 위치에 삽입
    return arr

my_list = test.copy()
print('정렬된 배열:', insertion_sort(my_list))
