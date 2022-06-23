import sys

input = lambda : sys.stdin.readline().rstrip()

n = int(input())
word = input()

pt = 0
result = 0
hidden_found = False
while pt < n:
    if word[pt].isdigit():
        hidden_found = True
        num = ''
        # pt의 범위 체크를 인덱스로서 사용하기 전에 써야 index Error를 방지할 수 있음
        # while not word[pt].isalpha() and pt < n 으로 쓰면
        while pt < n and word[pt].isdigit():
            num += word[pt]
            pt += 1
        result += int(num)

    pt += 1

if hidden_found:
    print(result)
else:
    print(0)

