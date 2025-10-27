from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        edge_zeros = [[False for _ in range(n)] for _ in range(m)]

        def dfs(x, y):
            edge_zeros[x][y] = True

            for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x + i, y + j
                if not (0 <= nx < m and 0 <= ny < n): continue
                if board[nx][ny] == "X": continue
                if edge_zeros[nx][ny]: continue

                dfs(nx, ny)
        
        for i in range(n):
            if board[0][i] == "O":
                dfs(0, i)
            if board[m - 1][i] == "O":
                dfs(m - 1, i)
        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n - 1] == "O":
                dfs(i, n - 1)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not edge_zeros[i][j]:
                    board[i][j] = "X"



if __name__ == "__main__":
    sol = Solution()
    sol.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]) # [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    sol.solve([["X"]]) # [["X"]]
