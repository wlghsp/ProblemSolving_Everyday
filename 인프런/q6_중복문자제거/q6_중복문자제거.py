



# ksekkset

s = list(input())

list = []
for i in range(len(s)):
    if s[i] not in list:
        list.append(s[i])

print(''.join(list))




