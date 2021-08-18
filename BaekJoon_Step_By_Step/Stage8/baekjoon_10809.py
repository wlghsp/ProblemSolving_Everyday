

s = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
for i in list(alphabet):
    if i in s:
        print(s.index(i), end=" ")
    else:
        print(-1, end=" ")
