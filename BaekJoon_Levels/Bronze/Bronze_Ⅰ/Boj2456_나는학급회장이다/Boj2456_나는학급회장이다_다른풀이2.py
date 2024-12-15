import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

point = [[1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0]]

for _ in range(N):
    a, b, c = map(int, input().split())
    point[0][a] += 1
    point[1][b] += 1
    point[2][c] += 1


# 총점 정렬을 따로 담아두지 않고도 동적으로 계산 후 비교하여 내림차순 정렬함
# 총점, 3점, 2점 내림차순 정렬
point = sorted(point, key=lambda x: (-(3 * x[3] + 2 * x[2] + x[1]), -x[3], -x[2]))

if point[0][1:] == point[1][1:]:
    print(0, 3*point[0][3] + 2 * point[0][2] + point[0][1])
else:
    print(point[0][0], 3*point[0][3] + 2*point[0][2] + point[0][1])
