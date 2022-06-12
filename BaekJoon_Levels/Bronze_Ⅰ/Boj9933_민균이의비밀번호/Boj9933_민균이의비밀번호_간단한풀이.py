import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())  # 단어의 수
words = [input() for _ in range(N)]

password = ""
for w in words:
    # 패스워드는 팰린드롬이거나, 거꾸로 된 단어가 따로 존재할 것
    # 따라서 단어를 거꾸로 만든 단어가 존재한다면, 팰린드롬이 있거나 거꾸로 된 수가 존재하는 것
    if w[::-1] in words:
        print(len(w), w[len(w)//2])
        break
