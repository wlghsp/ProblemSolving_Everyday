from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate([1, 3, 4, 2, 2]))  # 2
    print(s.findDuplicate([3, 1, 3, 4, 2]))  # 3
    print(s.findDuplicate([3, 3, 3, 3, 3]))  # 3
