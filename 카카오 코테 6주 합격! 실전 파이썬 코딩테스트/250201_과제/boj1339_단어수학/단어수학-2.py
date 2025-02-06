import sys

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
words = [input() for _ in range(N)]
word_dict = {}

for word in words:
    for i in range(len(word)):
        c = word[i]
        if c in word_dict:
            word_dict[c] += 10 ** (len(word) - 1 - i)
        else:
            word_dict[c] = 10 ** (len(word) -1 - i)

sorted_values = sorted(word_dict.values(), reverse=True)

result = 0
number = 9
for value in sorted_values:
    result += value * number
    number -= 1

print(result)