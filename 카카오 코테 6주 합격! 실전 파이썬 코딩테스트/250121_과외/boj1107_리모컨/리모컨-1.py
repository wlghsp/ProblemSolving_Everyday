
N = input()# 이동하려고 하는 채널
length = len(N)
N = int(N)
M = int(input()) # 고장난 버튼의 개수
remote_buttons = [i for i in range(10)]
broken = [False] * 10
cur = 100 # 현재 채널 100번

if M == 10:
    print(abs(cur - N))
    exit()
elif M == 0:
    print(length)
    exit()
elif M > 0:
    broken_buttons = list(map(int, input().split())) # 고장난 버튼 번호
    for button in broken_buttons:
        remote_buttons.remove(button)

min_cnt = abs(cur - N)
def recur(picked, depth, length):
    global min_cnt
    if depth == length:
        number = int(''.join(map(str, picked)))
        min_cnt = min(min_cnt, len(picked) + abs(N - number))
        return

    for i in remote_buttons:
        picked.append(i)
        recur(picked, depth + 1, length)
        picked.pop()


for i in range(1, 8):
    recur([], 0, i)

print(min_cnt)