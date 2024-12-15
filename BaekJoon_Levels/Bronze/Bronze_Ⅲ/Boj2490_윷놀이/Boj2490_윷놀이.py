import sys
input = lambda : sys.stdin.readline().rstrip()


for _ in range(3):
    yut = list(map(int, input().split()))
    deung = yut.count(1)
    if deung == 4:
        print("E")
    elif deung == 3:
        print("A")
    elif deung == 2:
        print("B")
    elif deung == 1:
        print("C")
    elif deung == 0:
        print("D")