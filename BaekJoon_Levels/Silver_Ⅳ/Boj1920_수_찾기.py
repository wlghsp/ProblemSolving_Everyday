


import sys

input = lambda : sys.stdin.readline().rstrip()

def bSearch(arr, key):
    lo = 0
    high = len(arr) - 1

    if lo <= high:
        mid = (lo+high) // 2
        if arr[mid] > key:
            high = mid - 1
        elif arr[mid] < key:
            lo = mid + 1
        else:
            return mid

    return -1


N = int(input())
arr = list(map(int, input().split()))
M = int(input())

# 꼭 정렬해야함. 이진탐색은 그러함.
arr.sort()

brr = list(map(int, input().split()))
for num in brr:
    print(1 if bSearch(arr, num) >= 0 else 0)

