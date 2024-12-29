
def is_palindrome(s):

    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False
    # 메모리 사용 비효율
    # 새로운 문자열을 만들기 때문
    return is_palindrome(s[1:-1])

res = is_palindrome("abba")
print(res)