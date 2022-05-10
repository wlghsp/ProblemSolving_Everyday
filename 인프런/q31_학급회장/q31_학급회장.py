
N = int(input())
s = input()

# hash로 풀이
dic = dict()

for c in list(s):
    if c in dic:
        dic[c] = dic.get(c) + 1
    else:
        dic[c] = 1
maxVal = max(list(dic.values()))

for k, v in dic.items():
    if v == maxVal:
        print(k)