"""

n개의 페어를 이용한 min(a,b) 의 합으로 만들 수 있는 가장 큰 수를 출력

"""


from typing import List


# 오름차순 풀이
def arrayPairSum(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2: # 두 수가 모이는 경우
            sum += min(pair)
            pair = [] # 페어 초기화 

    return sum


print(arrayPairSum([1,4,3,2])) # 4 