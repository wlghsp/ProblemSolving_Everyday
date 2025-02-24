"""
총감독은 한 시험장 감시 가능 B명
부감독관 한 시험장 감시 가능 C명

"""
N = int(input()) # 시험장의 개수
classes = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0

for c in classes:
    c -= B
    ans += 1
    if c > 0:
        ans += c // C + (1 if c % C != 0 else 0)

print(ans)