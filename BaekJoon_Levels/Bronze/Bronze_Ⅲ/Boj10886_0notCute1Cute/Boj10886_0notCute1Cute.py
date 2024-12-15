import sys
input = lambda : sys.stdin.readline().rstrip()

cute = 0
not_cute = 0
for _ in range(int(input())):
    vote = int(input())
    if vote == 1:
        cute += 1
    else:
        not_cute += 1

print("Junhee is cute!" if cute > not_cute else "Junhee is not cute!")