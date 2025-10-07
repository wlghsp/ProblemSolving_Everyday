

def solution(n, x, arr):
    l, r = 0, n - 1

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid + 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return -1


N, X = map(int, input().split())
a = list(map(int, input().split()))
print(solution(N, X, a))
