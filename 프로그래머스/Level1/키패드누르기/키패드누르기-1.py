def solution(numbers, hand):
    left_nums, right_nums = {1, 4, 7}, {3, 6, 9}
    # 1.키패드 위치 딕셔너리 만들기
    pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    pad_locs = {}
    for i in range(len(pad)):
        for j in range(len(pad[0])):
            pad_locs[pad[i][j]] = (i, j)

    left_loc, right_loc = pad_locs['*'], pad_locs['#']
    def mark_hand(number, hand_letter):
        answer.append(hand_letter)
        return pad_locs[number]

    def get_dist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def set_loc(number, left_dist, right_dist):
        nonlocal left_loc, right_loc
        if left_dist < right_dist or (left_dist == right_dist and hand == 'left'):
            left_loc = mark_hand(number, "L")
        else:
            right_loc = mark_hand(number, "R")

    answer = []
    for num in numbers:
        if num in left_nums:
            left_loc = mark_hand(num, "L")
        elif num in right_nums:
            right_loc = mark_hand(num, "R")
        else:  # 2, 5, 8, 0 이라면
            left_dist = get_dist(pad_locs[num], left_loc)
            right_dist = get_dist(pad_locs[num], right_loc)
            set_loc(num, left_dist, right_dist)

    return "".join(answer)


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))  # "LRLLLRLLRRL"
