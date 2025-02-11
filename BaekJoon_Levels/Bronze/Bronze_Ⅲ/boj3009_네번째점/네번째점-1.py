x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x_arr = [0] * 1001
y_arr = [0] * 1001

x_arr[x1] += 1
x_arr[x2] += 1
x_arr[x3] += 1
y_arr[y1] += 1
y_arr[y2] += 1
y_arr[y3] += 1
x4, y4 = -1, -1

for i in range(1001):
    if x_arr[i] == 1:
        x4 = i
    if y_arr[i] == 1:
        y4 = i
print(x4, y4)

