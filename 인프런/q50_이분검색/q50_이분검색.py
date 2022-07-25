import sys
input = lambda : sys.stdin.readline().rstrip()


def solution(m, arr):
    answer = 0
    arr.sort()
    lt, rt = 0, len(arr) - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if arr[mid] == m:
            answer = mid + 1
            break
        if arr[mid] > m: rt = mid - 1
        else: lt = mid + 1

    return answer


n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(solution(m, arr))