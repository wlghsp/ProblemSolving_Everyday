import sys
input = lambda : sys.stdin.readline().rstrip()
a, b = map(int, input().split())
arr = [0]
for i in range(46):
    for j in range(i):
        arr.append(i)

# sum + slicing 으로 구간합을 구함
print(sum(arr[a:b+1]))


