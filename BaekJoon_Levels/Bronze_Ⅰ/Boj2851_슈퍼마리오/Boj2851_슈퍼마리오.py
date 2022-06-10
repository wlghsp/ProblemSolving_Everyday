
import sys
input = lambda : sys.stdin.readline().rstrip()


arr = []
for i in range(10):
    arr.append(int(input()))

total = 0
answer = 0
for i in range(len(arr)):
    total += arr[i]
    if abs(100-answer) >= abs(100-total):
        answer = max(answer, total)


print(answer)