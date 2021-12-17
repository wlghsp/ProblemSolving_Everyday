
"""

전자 매장에는 부품이 N개 있고, 각 부품은 정수 형태의 고유한 번호가 있다. 부품 M개 종류가 모두 있는지 확인하는 프로그램을 작성해보자.

입력 예시
5
8 3 7 9 2
3
5 7 9

출력 예시
no yes yes


"""
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
store = list(map(int, input().split()))

m = int(input())     
partNums = list(map(int, input().split()))


def binary_search1(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid+1
    return None

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid -1)
    else:
        return binary_search(array, target, mid + 1, end)



for num in partNums:
    result = binary_search(store, num, 0, n-1)
    if result == None:
        print("no", end=' ')
    else:
        print("Yes", end=' ')