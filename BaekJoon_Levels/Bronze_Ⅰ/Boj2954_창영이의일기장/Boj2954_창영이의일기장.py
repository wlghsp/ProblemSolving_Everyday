import sys
input = lambda: sys.stdin.readline().rstrip()
sen = input()
answer = ""
vowels = "aeiou"
idx = 0
while True:
    if idx >= len(sen):
        break
    answer += sen[idx]
    if sen[idx] in vowels:
        idx += 2
    idx += 1

print(answer)