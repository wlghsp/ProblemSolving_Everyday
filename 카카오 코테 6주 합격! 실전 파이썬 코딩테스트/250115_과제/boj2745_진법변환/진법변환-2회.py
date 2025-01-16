

N, B = input().split()

B = int(B)

N = ''.join(reversed(N))
result = 0
for i in range(len(N)):
    c = N[i]
    if '0' <= c <= '9':
        num = ord(c) - ord('0')
    else:
        # 10부터 알파벳으로 시작하므로 10을 더해야함
        # A: 10, B: 11 ...
        num = ord(c) - ord('A') + 10

    result += num * (B ** i)

print(result)