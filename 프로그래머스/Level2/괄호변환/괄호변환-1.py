
def is_correct(s):
    cnt = 0
    for c in s:
        if c == ')':
            if cnt <= 0:
                return False
            else:
                cnt -= 1
        else:
            cnt += 1
    return True

def reverse(s):
    res = ''
    for c in s:
        if c == ')':
            res += '('
        else:
            res += ')'
    return res
def split_into_uv(s):
    count = 0
    u, v = '', ''
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            u = s[:i + 1]
            v = s[i + 1:]
            return u, v
    return u, v


def solution(p):
    if not p:
        return ''
    u, v = split_into_uv(p)

    if is_correct(u):
        return u + solution(v)

    answer = '('
    answer += solution(v)
    answer += ')'
    answer += reverse(u[1:-1])
    return answer

print(solution("(()())()")) # "(()())()"
print(solution(")(")) # "()"
print(solution("()))((()")) # "()(())()"
