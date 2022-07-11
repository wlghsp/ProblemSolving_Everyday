import sys

input = lambda: sys.stdin.readline().rstrip()

total = 0
arr = []
for _ in range(10):
    n = int(input())
    arr.append(n)

def Max_count(arr):
    d= {}
    key_value = set(arr)

    for k in key_value:
        cnt = arr.count(k)
        d[k] = cnt

    Max = 0
    result = []

    for i in d:
        if Max < d[i]:
            Max = d[i]
            keys = i
        # elif d[keys] == 1: # keys의 갯수가 1이라면 최빈값은 없음
        #     return None
    for j in d:
        if d[keys] == d[j]:
            result.append(j)

    print(result[0])

print(sum(arr) // 10)
Max_count(arr)
