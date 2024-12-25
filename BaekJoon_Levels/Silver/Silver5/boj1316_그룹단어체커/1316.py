import sys

input = lambda: sys.stdin.readline()[:-1]


N = int(input())

cnt = 0
for _ in range(N):
    word = input()
    chars = set()
    is_group_word = True
    for j in range(len(word)):
        cur = word[j]
        prev = word[j - 1]
        if j > 0 and cur != prev: # 이전 문자와 다른 경우
            if cur in chars:  # 이미 나온 적 있는 문자인 경우
                is_group_word = False
                break
            chars.add(word[j - 1]) # 이전 문자 추가
    if is_group_word:
        cnt += 1


print(cnt)
