

import sys

input = lambda : sys.stdin.readline().rstrip()


N = int(input())

arr = []

for _ in range(N):
    word = input()
    arr.append((len(word), word))

# arr = sorted(arr, key= lambda x: (x[0], x[1]))
arr = sorted(arr) # 람다로 정렬조건을 주지 않아도 알아서 첫 번째 길이와 두 번째 단어를 오름차순으로 정렬함.

print(arr[0][1])
for i in range(1, len(arr)):
   if arr[i][1] != arr[i-1][1]:
        print(arr[i][1])
