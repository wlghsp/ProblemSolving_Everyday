
arr = []

for i in range(9):
    arr.append(list(map(int, input().split())))

row, col = 0, 0
max_value = arr[row][col]

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_value:
            max_value = arr[i][j]
            row = i
            col = j
print(max_value)
print(row + 1, col + 1)