from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, index):
            if index == len(word):
                return True

            if not (0 <= r < rows and 0 <= c < cols): return False
            if board[r][c] != word[index]: return False

            temp = board[r][c]
            board[r][c] = '#'

            found = (dfs(r+1, c, index + 1) or 
                    dfs(r, c + 1, index + 1) or 
                    dfs(r - 1, c, index + 1) or 
                    dfs(r, c - 1, index + 1))

            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False


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
