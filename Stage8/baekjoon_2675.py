
a = int(input())

for _ in range(a):
    r, s = input().split()
    r = int(r)
    text = ""
    for i in s:
        text += i * r
    print(text)
