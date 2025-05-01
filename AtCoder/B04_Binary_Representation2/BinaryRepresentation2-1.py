
N = int(input())
str_N = str(N)
len_s = len(str_N)
# 2진수를 10진수로 변경
res = 0
for i in range(len_s - 1, -1, -1):
    if str_N[len_s - i - 1] == '1':
        res += 1 << i
print(res)
