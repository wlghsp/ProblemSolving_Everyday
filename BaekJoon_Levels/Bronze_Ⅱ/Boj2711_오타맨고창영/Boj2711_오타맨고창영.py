import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    a, word = input().split()
    word_list = list(word)
    a = int(a)
    del word_list[a-1]
    print(''.join(word_list))
