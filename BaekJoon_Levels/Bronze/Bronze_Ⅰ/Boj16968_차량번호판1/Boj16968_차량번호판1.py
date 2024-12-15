import sys

input = lambda: sys.stdin.readline().rstrip()

forms = {'c': 26, 'd': 10}

s = input()

answer = forms[s[0]]

for i in range(1, len(s)):
    mul = forms[s[i]]
    if s[i] == s[i - 1]:
        mul -= 1
    answer *= mul

print(answer)

'''
'c'는 문자가 위치하는 자리 26가지 가능
'd'는 숫자가 위치하는 자리이므로 10가지가 가능

연속해서 나타나는 경우는 c와 d 각각 (26-1), (10-1)가지 가능

c와 d일 때 가능한 수를  딕셔너리로 선언한 후, 조건문 대신 키 값을 찾아와 사용함.


'''
