def split_s(s, length):
    res = []
    idx = 0
    while idx < len(s):
        res.append(s[idx:idx + length])
        idx += length
    return res

def compress(splits):
    res = []
    idx = 0
    while idx < len(splits):
        cnt = 1
        curr = splits[idx]
        idx += 1
        while idx < len(splits) and curr == splits[idx]:
            cnt += 1
            idx += 1
        res.append(curr if cnt == 1 else (str(cnt) + curr))
    return ''.join(res)

def solution(s):
    answer = len(s)
    for i in range(1, len(s)):
        splits = split_s(s, i)
        compressed = compress(splits)
        answer = min(answer, len(compressed))
    return answer

print(solution("aabbaccc")) # 7
print(solution("a")) # 1