N, A, B, C, D = map(int, input().split())
shelters = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
min_distance = float('inf')

for t in range(C, D + 1):
    sam_x = A * t
    sam_y = B * t

    for sx, sy in shelters:
        dist = abs(sam_x - sx) + abs(sam_y - sy)
        min_distance = min(min_distance, dist)

print(min_distance)


"""
3 2 3 5 7
1 1
10 20
15 18

3
"""