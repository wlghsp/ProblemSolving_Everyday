import sys

input = lambda: sys.stdin.readline().rstrip()


def solve(s):
    answer = ""
    stk = []
    for c in s:
        # 닫는 괄호가 나오기 전에는 전부 집어 넣는다
        if c == ")":  # 닫는 괄호가 나오면
            while stk.pop() != "(":  # 전부 삭제한다. 여는 괄호가 나오면 종료
                None
        else:
            stk.append(c)

    for c in stk: answer += c

    return answer


s = input()
print(solve(s))
