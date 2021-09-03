"""
a 시작 값
d 등차의 값
n 몇번째 수 


"""

a, d, n = map(int, input().split())


i = a
count = 1
while True:
    i += d
    count += 1
    if count == n:
        break


print(i)
