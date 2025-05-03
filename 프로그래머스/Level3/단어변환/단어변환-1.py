def solution(begin, target, words):
    word_set = set(words)
    if target not in word_set:
        return 0
    len_words = len(words)
    visited = [False] * len_words

    answer = float('inf')
    def dfs(start, times):
        nonlocal answer
        if start == target:
            answer = min(answer, times)
            return

        for i in range(len(words)):
            if times >= len_words:
                return
            if visited[i]: continue
            if not is_convertible(start, words[i]): continue

            visited[i] = True
            dfs(words[i], times + 1)
            visited[i] = False

    dfs(begin, 0)
    return answer

def is_convertible(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt == 1


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4
