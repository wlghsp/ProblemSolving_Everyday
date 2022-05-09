



s = list(input())

lt, rt = 0, len(s) -1

# 투포인터
# lt는 0에서 시작, rt는 문자열의 끝에서 시작
while lt < rt:
    if not s[lt].isalpha: # lt위치가 알파벳 아니면 lt를 증가
        lt+=1
    elif not s[rt].isalpha: # rt위치가 알파벳이 아니면 rt를 감소
        rt-=1
    else: # 둘 다 알파벳인 경우
        s[rt], s[lt] = s[lt], s[rt]
        lt+=1
        rt-=1

print(''.join(s))
