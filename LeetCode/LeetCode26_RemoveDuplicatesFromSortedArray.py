from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if len(nums) <= 0:
        return 0

    curr = nums[0]
    cnt = 1

    for i in range(1, len(nums)):
        if curr != nums[i]:
            curr = nums[i]
            nums[cnt] = curr # 길이만 구하면 없어도 되지만, 배열 수정을 하라고 했으므로 필요함
            cnt+= 1

    return cnt

print(removeDuplicates([1,1,2]))