import sys
input = lambda : sys.stdin.readline().rstrip()
def solve(s):
    answer = ""
    stk = []
    for c in s:
        # 여는 괄호이거나 알파벳이면 스택에 집어넣는다
        if c == "(" or c.isalpha():
            stk.append(c)
        elif c == ")":
            while True:
                k = stk.pop()
                # 여는 괄호이면 전부 pop한 상태이므로 while문 종료
                if k == "(":
                    break
    for c in stk:
        answer += c

    return answer

s = input()
print(solve(s))