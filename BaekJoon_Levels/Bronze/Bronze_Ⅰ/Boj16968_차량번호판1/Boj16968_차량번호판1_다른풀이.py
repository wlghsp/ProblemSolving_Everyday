import sys

input = lambda: sys.stdin.readline().rstrip()

s = input()
if s[0] == 'c':
    answer = 26
else:
    answer = 10

for i in range(1, len(s)):
    if s[i] == 'c':
        if s[i - 1] == 'c':
            answer *= 25
        else:
            answer *= 26
    else:
        if s[i - 1] == 'd':
            answer *= 9
        else:
            answer *= 10

print(answer)

'''
'c'는 문자가 위치하는 자리 26가지 가능
'd'는 숫자가 위치하는 자리이므로 10가지가 가능

연속해서 나타나는 경우는 c와 d 각각 (26-1), (10-1)가지 가능

c와 d가 연속하는 경우를 알기 위해, 모든 조합을 조건문으로 작성 

'''
