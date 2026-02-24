from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = []
        for i in range(rowIndex + 1):
            curr = []
            for j in range(i + 1):
                if j == 0 or i == j:
                    curr.append(1)
                else:
                    p = prev[j - 1]
                    n = prev[j]
                    curr.append(p + n)
            prev = curr

        return prev


if __name__ == "__main__":
    s = Solution()

    # Test case 1: rowIndex = 3
    # Expected: [1, 3, 3, 1]
    print(s.getRow(3))

    # Test case 2: rowIndex = 0
    # Expected: [1]
    print(s.getRow(0))

    # Test case 3: rowIndex = 1
    # Expected: [1, 1]
    print(s.getRow(1))
