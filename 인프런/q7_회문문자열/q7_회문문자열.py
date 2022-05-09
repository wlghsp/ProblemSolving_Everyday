






# 내 풀이
# if str == str[::-1]:
#     print("YES")
# else:
#     print("NO")

# 자바 풀이 변환
str = input().lower()
def solution(str):
    for i in range(len(str) // 2): # 절반까지만 확인
        # 일치하지 않는 문자가 있다면 회문이 아님
        if str[i] != str[len(str) - 1 - i]: return "NO"
    return "YES"

print(solution(str))
