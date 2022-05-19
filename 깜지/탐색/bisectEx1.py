

'''
bisect_left(iterable, value): 왼쪽 인덱스를 구하기
bisect_right(iterable, value): 오른쪽 인덱스를 구하기
'''
from bisect import bisect_left, bisect_right


nums = [0,1,2,3,4,5,6,7,8,9]
n = 5

print(bisect_left(nums, n))
print(bisect_right(nums, n))

