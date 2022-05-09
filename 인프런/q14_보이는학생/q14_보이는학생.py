

N = int(input())

students = list(map(int, input().split()))

cnt = 1
max = students[0]
for i in range(1, len(students)):
    if students[i] > max:
        cnt+=1
        max = students[i]
print(cnt)