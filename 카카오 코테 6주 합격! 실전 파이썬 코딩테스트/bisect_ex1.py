from bisect import *

numbers = [1, 2, 2, 3, 3, 3, 5, 8, 11] # 정렬된 배열
query = 2
left = bisect_left(numbers, query)
right = bisect_right(numbers, query)
print(f'query: {query} -> bisect_left: {left}, bisect_right: {right}')
