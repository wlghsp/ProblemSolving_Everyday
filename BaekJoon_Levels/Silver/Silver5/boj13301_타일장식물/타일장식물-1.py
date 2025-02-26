N = int(input())
fibo = [0] * 81
fibo[0] = 0
fibo[1] = 1
for i in range(2, 81):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

print(fibo[N] * 2 + (fibo[N] + fibo[N - 1]) * 2)