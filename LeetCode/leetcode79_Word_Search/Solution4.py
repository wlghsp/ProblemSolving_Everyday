class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        def backtrack(x, y, index):
            if len(word) == index:
                return True
            
            if (not (0 <= x < n and 0 <= y < m)) or board[x][y] != word[index]:
                return False
            
            temp = board[x][y]
            board[x][y] = '#'
            found = (backtrack(x + 1, y, index + 1) or
                    backtrack(x, y + 1, index + 1) or 
                    backtrack(x - 1, y, index + 1) or
                    backtrack(x, y - 1, index + 1))
            board[x][y] = temp
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
    print(sol.exist(board1, "ABCCED"))  # Expected: True

    # Test 2
    board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print(sol.exist(board2, "SEE"))     # Expected: True

    # Test 3
    board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print(sol.exist(board3, "ABCB"))    # Expected: False

    # Test 4
    board4 = [["A"]]
    print(sol.exist(board4, "A"))       # Expected: True
