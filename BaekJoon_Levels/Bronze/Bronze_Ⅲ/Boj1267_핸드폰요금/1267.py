

def calculate(durations, seconds, per):
    cost = 0
    for d in durations:
       cost += (d // seconds + 1) * per
    return cost

N = int(input())
arr = list(map(int, input().split()))

young = calculate(arr, 30, 10)
minsik = calculate(arr, 60, 15)


if young > minsik:
    print('M', minsik)
elif minsik > young:
    print('Y', young)
else:
    print('Y M', young)

