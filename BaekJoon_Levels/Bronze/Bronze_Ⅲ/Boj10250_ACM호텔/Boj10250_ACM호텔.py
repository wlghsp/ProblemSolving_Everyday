import sys, math

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())
    floor = n % h
    if floor == 0: floor = h
    room_num = math.ceil(n / h)
    if room_num < 10:
        print(str(floor) + "0" + str(room_num))
    else:
        print(str(floor) + str(room_num))
