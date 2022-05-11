
import sys

input = lambda : sys.stdin.readline().rstrip()

dials = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

word = input()

answer = 0

for c in list(word):
    for i in range(len(dials)):
        if c in dials[i]:
            answer += i+3

print(answer)