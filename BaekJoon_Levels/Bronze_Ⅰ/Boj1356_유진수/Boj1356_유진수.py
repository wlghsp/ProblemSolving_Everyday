import sys
input = lambda : sys.stdin.readline().rstrip()

N = input()
n_len = len(N)
true = 0
for i in range(n_len-1):
    left = right = 1
    for j in range(i+1):
        left *= int(N[j])
    for k in range(i+1, n_len):
        right *= int(N[k])
    if left == right:
        print("YES")
        true = 1
        break
if true == 0:
    print("NO")


