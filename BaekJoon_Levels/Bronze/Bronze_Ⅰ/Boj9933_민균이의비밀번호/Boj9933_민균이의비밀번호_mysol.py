import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())  # 단어의 수
words = [input() for _ in range(N)]

password = ""
for w in words:
    if w == w[::-1] or any(w[::-1] == k for k in words):
        password = w
        break
print(len(password), password[len(password)//2])