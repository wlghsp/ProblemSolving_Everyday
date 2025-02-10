'''
N/2 마리 가져가도 좋다!
가장 많은 종류의 폰켓몬 갯수 출력
'''
def solution(nums):
    half_len = len(nums) // 2
    distinct_nums = set(nums)
    return min(half_len, len(distinct_nums))


print(solution([3, 1, 2, 3])) # 2
print(solution([3,3,3,2,2,4])) # 2
print(solution([3,3,3,2,2,2])) # 2