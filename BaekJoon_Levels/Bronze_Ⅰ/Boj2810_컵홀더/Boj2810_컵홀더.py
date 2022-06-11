import sys
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
seats = list(input())

# 다른사람 풀이
l = 0
for i in range(n):
    if seats[i] == 'L':
        l += 1
l //= 2
print(min(n+1-l, n))


## 내 풀이
result = ""
for i in range(n):
    if seats[i] == 'S':
        if result != "" and result[-1] == "*":
            result += seats[i] + "*"
        else:
            result += "*" + seats[i] + "*"
    elif seats[i] == 'L':
        if result != "" and result[-1] == 'L':
            result += seats[i] + "*"
        elif result == "":
            result += "*" + seats[i]
        else:
            result += seats[i]


cnt = result.count("*")
print(n if cnt > n else cnt)

