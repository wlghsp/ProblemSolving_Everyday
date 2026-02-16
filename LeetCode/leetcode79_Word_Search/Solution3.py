class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])


        def backtrack(r, c, index):
            if len(word) == index:
                return True
            
            if not (0 <= r < n and 0 <= c < m): return False
            if board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (backtrack(r + 1, c, index + 1) or
                     backtrack(r, c + 1, index + 1) or
                     backtrack(r - 1, c, index + 1) or
                     backtrack(r, c - 1, index + 1))
            
            board[r][c] = temp

            return found
            

        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True
        return False

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word1 = "ABCCED"
    print(sol.exist(board1, word1))  # Expected: True

    # Test 2
    board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word2 = "SEE"
    print(sol.exist(board2, word2))  # Expected: True

    # Test 3
    board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word3 = "ABCB"
    print(sol.exist(board3, word3))  # Expected: False

    # Test 4
    board4 = [["A"]]
    word4 = "A"
    print(sol.exist(board4, word4))  # Expected: True
