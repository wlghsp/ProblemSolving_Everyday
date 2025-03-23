from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # step 1. 정렬
        result = []

        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: # 중복된 i 값 스킵
                continue

            left, right = i + 1, n - 1 # step 2. 투 포인터 설정
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]]) # 정답 저장
                    left += 1
                    right -= 1

                    # Step 3. 중복 제거 (left, right 중복 값 스킵)
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total > 0:
                    left += 1 # 합이 작으면 left 증가 (큰 값 필요)
                else:
                    right -= 1 # 합이 크면 right 감소 (작은 값 필요)

        return result