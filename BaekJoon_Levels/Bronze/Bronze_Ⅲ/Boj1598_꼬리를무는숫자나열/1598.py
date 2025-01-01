

a, b = map(int, input().split())
a, b = a - 1, b - 1
ay, ax = a % 4, a // 4
by, bx = b % 4, b // 4

print(abs(ax - bx) + abs(ay - by))