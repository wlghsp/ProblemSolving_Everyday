import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())

s = input()
stk = []
val = []
for _ in range(N):
    val.append(int(input()))

# ord(문자) : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
# chr(정수) : 하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환합니다.

for ch in s:
    if ch.isalpha():
        stk.append(val[ord(ch) - ord('A')])
    else:
        b = stk.pop()
        a = stk.pop()
        if ch == '+':
            stk.append(a+b)
        elif ch == '-':
            stk.append(a-b)
        elif ch == '*':
            stk.append(a * b)
        elif ch == '/':
            stk.append(a / b)

print(f'{stk[0]:.2f}')