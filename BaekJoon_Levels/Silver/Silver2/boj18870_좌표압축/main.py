import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))

# 중복 제거 및 정렬
distinct = sorted(set(arr))

# 사전 생성
coordinate_map = {value: index for index, value in enumerate(distinct)}

# 최종 출력
print(' '.join(str(coordinate_map[n]) for n in arr))