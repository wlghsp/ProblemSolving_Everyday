






s = "ababbaab"

arr = list(s)

for i in range(1, len(arr) - 1):
    if arr[i - 1] > arr[i]:
        arr[i - 1], arr[i] = arr[i], arr[i - 1]



print(''.join(arr)) #




