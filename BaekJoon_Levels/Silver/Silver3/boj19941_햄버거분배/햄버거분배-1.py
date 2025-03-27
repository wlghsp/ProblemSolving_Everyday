N, K = map(int, input().split())
table = list(input())

# 왼쪽 K 거리에 햄버거 있는지 확인하고 가장 멀리에 있는 햄버거를 먹는다.
# 왼쪽에 없다면 오른쪽을 확인해서 먹는다.
# 햄버거를 먹으면 '0' 으로 바꿔놓는다.
cnt = 0
for i in range(N):
    if table[i] == 'P':
        # 왼쪽 확인
        found = False
        for j in range(max(0, i - K), i):
            if table[j] == 'H' and not found:
                found = True
                cnt += 1
                table[j] = '0'
                break
        if found: continue

        for j in range(i + 1, min(N, i + K + 1)):
            if table[j] == 'H' and not found:
                cnt += 1
                table[j] = '0'
                break
print(cnt)