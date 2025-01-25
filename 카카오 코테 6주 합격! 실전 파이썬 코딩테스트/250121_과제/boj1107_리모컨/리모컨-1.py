
N = input()# 이동 하려고 하는 채널
length = len(N)
N = int(N)
M = int(input()) # 고장난 버튼의 개수
remote_buttons = [i for i in range(10)]
cur = 100 # 현재 채널 100번

if M == 10: # 전부 고장난 경우 +, - 로 이동
    print(abs(cur - N))
elif M == 0: # 고장난 버튼이 없는 겨우
    # 번호를 눌러 가는 경우와 +, -로 이동 하는 경우 횟수 비교 필요
    print(min(length, abs(cur - N)))
else:
    broken_buttons = list(map(int, input().split())) # 고장난 버튼 번호 입력

    for button in broken_buttons: # 고장난 버튼 번호 삭제
        remote_buttons.remove(button)

    min_cnt = abs(cur - N) # 최소 횟수 100 번에서 시작 하는 경우로 초기화

    # 중복 순열 생성
    def recur(picked, depth, length):
        global min_cnt

        if depth == length:
            number = int(''.join(map(str, picked)))
            min_cnt = min(min_cnt, length + abs(N - number))
            return

        for i in remote_buttons:
            picked.append(i)
            recur(picked, depth + 1, length)
            picked.pop()


    # 찾는 숫자 보다 큰 경우를 찾기 위해 찾는 숫자 길이 + 1 까지 생성
    for i in range(1, length + 2):
        recur([], 0, i)

    print(min_cnt)