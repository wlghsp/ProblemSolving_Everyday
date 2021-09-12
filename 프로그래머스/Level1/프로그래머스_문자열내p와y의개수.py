def solution(s):
    return s.lower().count("p") == s.lower().count("y")


s = "pPoooyY"
print(solution(s))
