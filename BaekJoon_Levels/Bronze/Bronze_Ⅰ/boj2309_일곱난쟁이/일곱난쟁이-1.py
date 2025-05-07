heights = [int(input()) for _ in range(9)]
heights.sort()
height_total = sum(heights)

for i in range(9):
    for j in range(i, 9):
        left = height_total - heights[i] - heights[j]
        if left == 100:
            for k in range(9):
                if k != i and k != j:
                    print(heights[k])
            exit(0)
