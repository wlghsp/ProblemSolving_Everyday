import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
words = [input() for _ in range(N)]

word_map = {}
for word in words:
    len_w = len(word) - 1
    for i in range(len(word)):
        if word[i] in word_map:
            cur = word_map.get(word[i])
            word_map[word[i]] = 10 ** len_w + cur
        else:
            word_map[word[i]] = 10 ** len_w
        len_w -= 1

sorted_word_map = dict(sorted(word_map.items(), reverse=True, key=lambda item: item[1]))

number = 9
for k in sorted_word_map.keys():
    sorted_word_map[k] = str(number)
    number -= 1

result = 0
for word in words:
    num = ""
    for i in range(len(word)):
        num += sorted_word_map.get(word[i])
    result += int(num)
print(result)