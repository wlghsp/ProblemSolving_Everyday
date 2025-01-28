N = int(input())
arr = list(map(int, input().split()))

left, right = 0, len(arr) - 1
left_ans, right_ans = 0, 0
min_mix_val = float('inf')

while left < right:
    # 주의: 미리 mix_val을 절대값으로 변경할 경우 아래에서 인덱스 변경할 시 오류 가능성 있음
    mix_val = arr[left] + arr[right]
    if min_mix_val > abs(mix_val):
        min_mix_val = abs(mix_val)
        left_ans, right_ans = arr[left], arr[right]

    if mix_val < 0:
        left += 1
    elif mix_val > 0:
        right -= 1
    else:
        break
print(left_ans, right_ans)