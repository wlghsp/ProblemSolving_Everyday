
N, K = input().split()
nums = input().split()

result = 0
def recur(picked, length):
    global result
    if len(picked) == length:
        number = int(''.join(picked))
        if int(N) >= number:
            result = max(result, number)
        return

    for i in range(int(K)):
        recur(picked + [nums[i]], length)

for i in range(1, len(N) + 1):
    recur([], i)
print(result)
