def solution(word):
    answer = 1
    vowels = "AEIOU"
    words = []
    def get_word(indexes):
        res = []
        for idx in indexes:
            res.append(vowels[idx])
        return "".join(res)

    def recur(picked):
        if picked:
            words.append(get_word(picked))

        if len(picked) == 5:
            return

        for i in range(5):
            recur(picked + [i])
    recur([])
    words.sort()

    for w in words:
        if w == word:
            return answer
        answer += 1
    return answer

print(solution("AAAAE")) # 6
print(solution("AAAE")) # 10
print(solution("I")) # 1563
print(solution("EIO")) # 1189