def recur(picked, start, arr, length):
    if len(picked) == length:
        print(*picked)
        return

    for i in range(start, len(arr)):
        picked.append(arr[i])
        recur(picked, i + 1, arr, length)
        picked.pop()


while True:
    input_str = input()
    if input_str == '0':
        break
    s = list(map(int, input_str.split()))
    recur([], 0, s[1:], 6)
    print()
