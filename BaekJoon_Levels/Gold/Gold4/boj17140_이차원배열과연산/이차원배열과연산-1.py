from collections import Counter

R, C, K = map(int, input().split())
R, C = R - 1, C - 1
A = [list(map(int, input().split())) for _ in range(3)]

def solve(A):
    time = 0
    while True:
        if time > 100:
            return -1
        if (R < len(A) and C < len(A[0])) and A[R][C] == K:
            return time

        # 1. R, C 연산
        r, c = len(A), len(A[0])
        if r >= c:
            # 모든 행 정렬
            max_row = 0
            for row in A:
                no_zero = [num for num in row if num != 0]
                count_dict = Counter(no_zero)
                sorted_count = sorted(count_dict.items(), key=lambda x:(x[1], x[0]))

                new_row = []
                for num, cnt in sorted_count:
                    new_row.extend([num, cnt])
                row[:] = new_row
                max_row = max(len(row), max_row)

            # max > 100 -> max = 100
            max_row = min(100, max_row)

            # 가장 큰 행 기준으로 모든 행의 크기 변경
            for row in A:
                row.extend([0] * (max_row - len(row)))

        else:
            # 모든 열 정렬
            max_col = 0
            sorted_cols = []
            for j in range(c):
                col = []
                for i in range(r):
                    if A[i][j] != 0:
                        col.append(A[i][j])
                count_dict = Counter(col)
                sorted_count = sorted(count_dict.items(), key=lambda x: (x[1], x[0]))

                new_col = []
                for num, cnt in sorted_count:
                    new_col.extend([num, cnt])
                sorted_cols.append(new_col)

                max_col = max(len(new_col), max_col)


            max_col = min(100, max_col)
            # 가장 큰 열 기준으로 모든 열의 크기 변경
            A = [[0] * c for _ in range(max_col)]
            for i in range(len(sorted_cols)):
                for j in range(len(sorted_cols[i])):
                    A[j][i] = sorted_cols[i][j]

        time += 1


print(solve(A))