

n = int(input())

s = input()

answer = ""

for _ in range(n):
    tmp = s[:7].replace('#', '1').replace('*', '0')
    num = int(tmp, 2)
    answer += chr(num) # chr은 숫자를 문자로, ord는 문자를 숫자로
    s = s[7:]

print(answer)