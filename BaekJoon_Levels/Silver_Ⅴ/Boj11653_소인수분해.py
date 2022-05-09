import sys, math

input = lambda : sys.stdin.readline().rstrip()


N = int(input())

for i in range(2, int(math.sqrt(N))+1):
    while N % i == 0:
        print(i)
        N /= i


if N!= 1:
    print(int(N))

#
# d= 2
# while N != 1:
#     if N % d != 0:
#         d += 1
#     else:
#         N //= d
#         print(d)
#


