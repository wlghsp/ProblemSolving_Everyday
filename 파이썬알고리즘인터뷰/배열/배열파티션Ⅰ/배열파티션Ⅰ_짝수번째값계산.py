"""

n개의 페어를 이용한 min(a,b) 의 합으로 만들 수 있는 가장 큰 수를 출력

"""


from typing import List


# 짝수번째 값 계산
def arrayPairSum(nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum


print(arrayPairSum([1,4,3,2])) # 4 