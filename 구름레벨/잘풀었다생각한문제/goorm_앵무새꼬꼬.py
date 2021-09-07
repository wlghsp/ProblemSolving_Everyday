"""
Hello, World!
I'm your father
What are you doing here?

그냥 어려워보였는데 시간 조금 들여서 풀어서 기뻐서 이 폴더에 들어옴 
단지 기분 좋아서...
"""

import sys

input = sys.stdin.readline


n = int(input())


sentences = []
for _ in range(n):
    sentences.append(input())

result = []
for sentence in sentences:
    sentence = list(sentence)
    temp = []
    for letter in sentence:
        temp_letter = letter.lower()
        if (
            temp_letter == "a"
            or temp_letter == "e"
            or temp_letter == "i"
            or temp_letter == "o"
            or temp_letter == "u"
        ):
            temp.append(letter)
    if temp:
        result.append(temp)
    else:
        result.append("???")


for list in result:
    print("".join(list))
