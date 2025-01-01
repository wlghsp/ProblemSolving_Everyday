
vowels = {'a', 'e', 'i', 'o', 'u'}

while True:
    sentence = input().lower()
    if sentence == '#':
        break
    cnt = 0
    for c in sentence:
        if c in vowels:
           cnt += 1
    print(cnt)
