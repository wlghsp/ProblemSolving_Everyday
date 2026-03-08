from collections import defaultdict
from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)

        num_dict = defaultdict(list)
        for i in range(n):
            for j in range(len(nums[i])):
                k = i + j
                num_dict[k].append(nums[i][j])
        
        sorted_dict = sorted(num_dict.items(), key=lambda v:v[0])
        
        result = []
        for k, v in sorted_dict:
            for a in v[::-1]:
                result.append(a)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
    # [1,4,2,7,5,3,8,6,9]

    print(sol.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))
    # [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
