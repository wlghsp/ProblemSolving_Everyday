
def get_insert_loc(nums, target):
    left, right = 0, len(nums)
    while left < right: # left 와 right 가 만나는 지점이 target 값 이상이 처음 나오는 위치
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid


    return right


P = int(input())
result = []
for i in range(P):
    input_str = input()
    n, *heights = list(map(int, input_str.split()))
    sorted_heights = [heights[0]]
    cnt = 0
    for height in heights[1:]:
        loc = get_insert_loc(sorted_heights, height)
        cnt += len(sorted_heights) - loc
        sorted_heights.insert(loc, height)
    result.append((n, cnt))

for n, cnt in result:
    print(n, cnt)