import sys
input = lambda : sys.stdin.readline().rstrip()


def bSearch(arr, key):
    lo = 0
    high = len(arr) - 1

    while lo <= high:
        mid = (lo+high) // 2
        if arr[mid] > key:
            high = mid - 1
        elif arr[mid] < key:
            lo = mid + 1
        else:
            return mid
    return -1

N = int(input())

arr = [i for i in list(map(int, input().split()))]

M = int(input())

b = [i for i in list(map(int, input().split()))]

arr.sort()



for i in range(M):
    if bSearch(arr, b[i]) >= 0:
        print(1, end=' ')
    else:
        print(0, end=' ')