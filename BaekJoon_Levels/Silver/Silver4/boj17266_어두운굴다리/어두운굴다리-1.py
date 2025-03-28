N = int(input())  # 굴다리의 길이 N
M = int(input())  # 가로등의 개수 M
lamp_locs = list(map(int, input().split()))  # M개의 가로등의 위치

# 굴다리의 길이 N 을 모두 비추기 위한 가로등의 최소 높이
# 덮을 수 있는 높이를 구해 놓고 최댓값 출력

# 1. 0에서 첫번째 램프까지, 마지막 램프에서 N까지 거리
distances = [lamp_locs[0], N - lamp_locs[-1]]

# 2. 램프 사이 거리 구하기, 램프 사이는 양쪽에서 비추므로 거리를 2로 나눔 홀수인 경우 1을 더함
for i in range(1, len(lamp_locs)):
    dist = lamp_locs[i] - lamp_locs[i - 1]
    distances.append(dist // 2 if dist % 2 == 0 else dist // 2 + 1)
print(max(distances))
