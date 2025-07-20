from collections import deque


def solution(rows, columns, queries):
    answer = []
    matrix = [[0] * columns for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = num
            num += 1

    def rotate(x1, y1, x2, y2):
        dq = deque()
        for i in range(y1, y2):
            dq.append(matrix[x1][i])
        for i in range(x1, x2):
            dq.append(matrix[i][y2])
        for i in range(y2, y1, -1):
            dq.append(matrix[x2][i])
        for i in range(x2, x1, -1):
            dq.append(matrix[i][y1])

        dq.appendleft(dq.pop())
        min_val = float('inf')

        for i in range(y1, y2):
            val = dq.popleft()
            matrix[x1][i] = val
            min_val = min(min_val, val)
        for i in range(x1, x2):
            val = dq.popleft()
            matrix[i][y2] = val
            min_val = min(min_val, val)
        for i in range(y2, y1, -1):
            val = dq.popleft()
            matrix[x2][i] = val
            min_val = min(min_val, val)
        for i in range(x2, x1, -1):
            val = dq.popleft()
            matrix[i][y1] = val
            min_val = min(min_val, val)

        answer.append(min_val)

    for a, b, c, d in queries:
        rotate(a - 1, b - 1, c - 1, d - 1)
    return answer



print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])) # [8, 10, 25]