from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        cnt = 0
        N = len(baskets)
        used = [False] * N
        for f in fruits:
            for i in range(N):
                if f <= baskets[i] and not used[i]:
                    used[i] = True
                    cnt += 1
                    break

        return N - cnt


if __name__ == "__main__":
    sol = Solution()
    print(sol.numOfUnplacedFruits([4, 2, 5], [3,5,4])) # 1
    print(sol.numOfUnplacedFruits([3,6,1], [6, 4, 7])) # 0
