
N = input()
len_N = len(N)
N = int(N)
M = int(input())
buttons = [i for i in range(0, 10)]
cur = 100

if M == 10:
    print(abs(cur - N))
elif M == 0:
    print(min(abs(cur - N), len_N))
else:
    broken_buttons = list(map(int, input().split()))
    for b in broken_buttons:
        buttons.remove(b)

    min_button_push_cnt = abs(cur - N)

    def recur(picked, depth, length):
        global min_button_push_cnt
        if depth == length:
            number = int(''.join(map(str, picked)))
            min_button_push_cnt = min(min_button_push_cnt, len(picked) + abs(number - N))
            return

        for i in buttons:
            picked.append(i)
            recur(picked, depth + 1, length)
            picked.pop()

    for i in range(1, len_N + 2):
        recur([], 0, i)

    print(min_button_push_cnt)