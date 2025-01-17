

N, B = input().split()
B = int(B)
N = "".join(reversed(N))
alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0
for i in range(len(N)):
    result += alpha.index(N[i]) * (B ** i)
print(result)