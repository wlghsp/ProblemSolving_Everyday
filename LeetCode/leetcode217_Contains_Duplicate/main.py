from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distincts = set()

        for n in nums:
            if n in distincts:
                return True
            distincts.add(n)

        return False