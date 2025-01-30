N = int(input())
cnt = 0
for _ in range(N):
    word = input()
    word_set = set()
    prev = word[0]
    word_set.add(prev) # 미리 담아 놓음
    is_group_word = True
    for i in range(1, len(word)):
        if prev != word[i]:
            if word[i] not in word_set: # 새로운 문자가 없는 경우만 담고
                word_set.add(word[i])
            else:
                is_group_word = False # 그룹단어가 아님
                break # 그룹단어가 아니므로 바로 반복문 종료
            prev = word[i]
    if is_group_word:
        cnt += 1

print(cnt)