def solution(wallpaper):
    min_r, min_c = len(wallpaper), len(wallpaper[0])
    max_r, max_c = -1, -1
    for r, row in enumerate(wallpaper):
        for c, cell in enumerate(row):
            if cell == "#":
                min_r = min(min_r, r)
                min_c = min(min_c, c)
                max_r = max(max_r, r)
                max_c = max(max_c, c)

    return [min_r, min_c, max_r + 1, max_c + 1]

print(solution(
    [".#...",
     "..#..",
     "...#."]
)) # [0, 1, 3, 4]