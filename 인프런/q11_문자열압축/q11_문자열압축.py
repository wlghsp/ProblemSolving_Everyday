

s = input()


s = s + " " # 첫 번째 if 조건을 위해 뒤에 한 칸 넣어줌

answer = ""
cnt = 1

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:  # 같은 알파벳
        cnt += 1 # cnt 증가
    else: # 다른 알파벳
        # 다른 알파벳이므로 알파벳을 붙이고 1보다 크면 빈도를 붙여줘야 함.
        answer += s[i]
        if cnt > 1: answer += str(cnt)
        cnt = 1 # cnt를 1로 초기화

print(answer)