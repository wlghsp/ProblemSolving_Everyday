from collections import Counter


def get_multi_set(str):
    return [str[i:i + 2].upper() for i in range(len(str) - 1) if str[i].isalpha() and str[i + 1].isalpha()]


def solution(str1, str2):
    a, b = get_multi_set(str1),get_multi_set(str2)
    if not a and not b:
        return 65536

    a_count, b_count = Counter(a), Counter(b)

    inter_len = sum(min(a_count[k], b_count[k]) for k in a_count.keys() & b_count.keys())
    union_len = sum(max(a_count[k], b_count[k]) for k in a_count.keys() | b_count.keys())
    result = inter_len / union_len
    answer = int(result * 65536)
    return answer


print(solution("FRANCE", "french")) # 16384
print(solution("handshake", "shake hands")) # 65536
print(solution("aa1+aa2", "AAAA12")) # 43690
print(solution("E=M*C^2", "e=m*c^2")) # 65536
print(solution("", "")) # 65536