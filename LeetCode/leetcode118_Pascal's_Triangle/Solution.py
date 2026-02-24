from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    prev = result[i - 1][j - 1]
                    next = result[i - 1][j]
                    row.append(prev + next)
            result.append(row)

        return result                


if __name__ == "__main__":
    s = Solution()

    # Test case 1: numRows = 5
    # Expected: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    print(s.generate(5))

    # Test case 2: numRows = 1
    # Expected: [[1]]
    print(s.generate(1))
