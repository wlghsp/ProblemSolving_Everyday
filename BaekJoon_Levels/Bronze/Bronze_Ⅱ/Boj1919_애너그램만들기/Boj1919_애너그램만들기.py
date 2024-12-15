import sys

input = lambda: sys.stdin.readline().rstrip()

lst = [0] * 26
# 소문자 알파벳의 빈도수를 +, - 하여 이들의 절댓값을 합하면
# 일치하는 문자를 제외한 빼야될 문자 수가 나온다.
for i in list(input()):
    lst[ord(i) - 97] += 1
for j in list(input()):
    lst[ord[j] - 97] -= 1
print(sum(map(abs, lst)))
