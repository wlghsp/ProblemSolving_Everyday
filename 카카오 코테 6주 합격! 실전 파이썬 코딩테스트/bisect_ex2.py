from bisect import *

numbers = [1, 2, 2, 3, 3, 3, 5, 6, 8, 11] # 정렬된 배열
queries = [0, 4, 15]

for query in queries:
    left = bisect_left(numbers, query)
    right = bisect_right(numbers, query)
    print(f'query: {query} -> bisect_left: {left}, bisect_right: {right}')

# 배열 안에 타겟이 없을 때, 따로 알려주지 않음 (그럴듯한 index를 반환)
#   binary_left 의 값으로 일치 여부를 확인해야 함
#   if (arr[left] == element):
