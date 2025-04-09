def solution(word):
    answer = 1
    vowels = "AEIOU"
    words = []

    def recur(picked):
        if picked:
            words.append(''.join(vowels[i] for i in picked))

        if len(picked) == 5:
            return

        for i in range(5):
            picked.append(i)
            recur(picked)
            picked.pop()

    recur([])

    # words.sort() 생성 시 사전순이므로 정렬 필요 없음

    for w in words:
        if w == word:
            return answer
        answer += 1
    return words.index(word) + 1

print(solution("AAAAE")) # 6
print(solution("AAAE")) # 10
print(solution("I")) # 1563
print(solution("EIO")) # 1189