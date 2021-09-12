def solution(s):
    return s.isdigit() and len(s) in [4, 6] 


s = "1234"

print(solution(s))
