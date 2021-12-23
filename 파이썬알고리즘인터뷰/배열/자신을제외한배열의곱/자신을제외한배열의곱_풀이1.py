

"""
배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라 
[1,2,3,4]

[24,12,8,6]



Input: nums = [-1,1,0,-3,3]


Output: [0,0,9,0,0]


"""
from typing import List


# 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈 


def productExceptSelf(nums: List[int]) -> List[int]:
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(len(nums)):
        out.append(p)
        p = p * nums[i]
    
    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums) -1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]


    return out







print(productExceptSelf([1,2,3,4]))