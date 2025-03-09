from collections import defaultdict


def solution(s):
    num_count = defaultdict(int)
    num = []
    for i in range(len(s) - 1):
        if s[i].isdigit():
            num.append(s[i])
        elif (s[i] == ',' and s[i + 1] != '}') or (s[i] == '}' and s[i + 1] != ','):
            number = int("".join(num))
            num_count[number] += 1
            num = []
    sorted_num_count = sorted(num_count.items(), key=lambda x: x[1], reverse=True)

    return [a[0] for a in sorted_num_count]


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")) # [2, 1, 3, 4]
print(solution("{{20,111},{111}}")) # [111,20]
print(solution("{{123}}")) # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) # [3,2,4,1]