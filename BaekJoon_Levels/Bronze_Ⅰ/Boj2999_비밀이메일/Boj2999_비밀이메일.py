import sys

input = lambda: sys.stdin.readline().rstrip()

'''
1. R과 C를 찾는다. C보다 작은 R의 최댓값을 찾는다. 
2. R*C 배열을 생성한다. 
3. 1행 1열 2행 1열 ...이런 식으로 행렬에 옮긴다.위 아래 위 아래 이런 식으로 옮긴다. 
4. 다시 이 배열의 행의 왼쪽부터 오른쪽으로 읽어 만든 문장을 출력한다. 
'''


def getRC(n):
    maxR = 0
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0 and maxR < i <= n // i:
            maxR = i
    return maxR, (n // maxR)


message = input()
# 1. R과 C를 찾는다. C보다 작은 R의 최댓값을 찾는다.
N = len(message)
R, C = getRC(N)
# 2. R*C 배열을 생성한다.
matrix = [[0 for _ in range(C)] for _ in range(R)]
# 3. 1행 1열 2행 1열 ...이런 식으로 행렬에 옮긴다.위 아래 위 아래 이런 식으로 옮긴다.

# idx = 0
# for i in range(C):
#     for j in range(R):
#         matrix[j][i] = message[idx]
#         idx += 1
#
# result = ""
# for i in range(R):
#     for j in range(C):
#         result += matrix[i][j]

# print("".join([message[i * R + j] for j in range(R) for i in range(C)]))
for i in range(R):
    print(message[i::R], end='')