import sys

input = lambda: sys.stdin.readline().rstrip()


def solve(board, moves):
    answer = 0
    stk = []
    for c in moves:
        for i in range(len(board)):
            if board[i][c - 1] != 0:
                num = board[i][c - 1]
                board[i][c - 1] = 0

                if num in stk:
                    if stk[-1] == num:
                        stk.pop()
                        answer += 2
                    else: stk.append(num)
                else: stk.append(num)

                break
    return answer

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
moves = list(map(int, input().split()))
print(solve(board, moves))

