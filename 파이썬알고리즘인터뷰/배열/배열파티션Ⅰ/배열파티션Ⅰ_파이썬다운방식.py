"""

n개의 페어를 이용한 min(a,b) 의 합으로 만들 수 있는 가장 큰 수를 출력

"""


from typing import List


# 파이썬다운 방식
def arrayPairSum(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])


print(arrayPairSum([1,4,3,2])) # 4 