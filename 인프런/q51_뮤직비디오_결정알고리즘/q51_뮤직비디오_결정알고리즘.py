import sys

input = lambda: sys.stdin.readline().rstrip()


def count(arr, capacity):
    cnt, sum = 1, 0

    for x in arr:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x

    return cnt


def solution(n, m, arr):
    answer = 0
    lt = max(arr)
    rt = sum(arr)

    while lt <= rt:
        mid = (lt + rt) // 2
        if count(arr, mid) <= m:
            answer = mid
            rt = mid - 1
        else:
            lt = mid + 1

    return answer


n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(solution(n, m, arr))
