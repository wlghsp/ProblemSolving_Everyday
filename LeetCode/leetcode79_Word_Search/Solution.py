from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    board1 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word1 = "ABCCED"
    result1 = solution.exist(board1, word1)
    print(f"Test 1: {result1}")  # Expected: True

    # Test case 2
    board2 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word2 = "SEE"
    result2 = solution.exist(board2, word2)
    print(f"Test 2: {result2}")  # Expected: True

    # Test case 3
    board3 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word3 = "ABCB"
    result3 = solution.exist(board3, word3)
    print(f"Test 3: {result3}")  # Expected: False

    # Test case 4
    board4 = [['a']]
    word4 = "a"
    result4 = solution.exist(board4, word4)
    print(f"Test 4: {result4}")  # Expected: True
