
def solution(n, target, arr):
    l, r = 0, n

    while l < r:
        mid = l + (r - l) // 2

        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l

N = int(input())
a = list(map(int, input().split()))
Q = int(input())
a.sort()

while Q > 0:
    x = int(input())

    print(solution(N, x, a))

    Q -= 1