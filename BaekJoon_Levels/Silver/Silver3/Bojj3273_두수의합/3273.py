N = int(input())
arr = list(map(int, input().split()))
X = int(input())
arr.sort()

left, right = 0, len(arr) - 1
cnt = 0

while left < right: # left, right 가 같은 경우는 두 포인터가 같은 요소를 가리키므로 불필요한 비교
    current_sum = arr[left] + arr[right]
    if current_sum == X:
        cnt += 1
        left += 1
        right -= 1
    elif current_sum < X:
        left += 1
    else:
        right -= 1

print(cnt)

'''
완전탐색은 O(N^2)으로 10^10 이므로 2*10^7 을 넘어서므로 TLE

시간복잡도는 정렬 O(NlogN)
투포인터 O(N) 전체 시간복잡도는 O(NlogN) 

'''