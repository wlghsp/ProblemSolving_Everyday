import sys

input = lambda: sys.stdin.readline()[:-1]


N = int(input())
words = [ input() for _ in range(N)]

ans = 0

for word in words:
    prev = word[0]
    before = set()
    isGroup = True


    for i in range(1, len(word)):  # 첫 문자는 이미 처리했으므로 1부터 시작
        if word[i] != prev:  # 연속된 문자가 아니면
            if word[i] in before:  # 이미 나온 문자라면 그룹 단어 아님
                isGroup = False
                break
            before.add(prev)  # 이전 문자를 집합에 추가
        prev = word[i]  # 현재 문자를 이전 문자로 설정

    if isGroup:
        ans += 1

print(ans)
