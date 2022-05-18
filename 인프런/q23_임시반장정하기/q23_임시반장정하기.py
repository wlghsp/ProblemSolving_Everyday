
N = int(input())

list = []

for _ in range(N):
    list.append([*map(int, input().split())])


for x in list:
    x.insert(0, 0)
list.insert(0, [0] * 6)
print(list)

answer = 0
maxVal = float("-inf")

for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        for k in range(1, 6):
            if list[i][k] == list[j][k]:
                cnt += 1
                break


    if cnt > maxVal:
        maxVal = cnt
        answer = i

print(answer)




