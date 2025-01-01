

arr = []
for i in range(9):
    arr.append(int(input()))

max_value = max(arr)
print(max_value)
for i,v in enumerate(arr):
    if v == max_value:
        print(i + 1)