N = int(input())

result = 1
cnt = 1

while True:
    if result >= N:
        print(cnt)
        break
    result += 6 * cnt
    cnt += 1
