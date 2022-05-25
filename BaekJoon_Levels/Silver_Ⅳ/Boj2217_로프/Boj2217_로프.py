
import sys
input = lambda : sys.stdin.readline().rstrip()



N = int(input())

rope = []
value = []
for i in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)

for i in range(N):
    value.append(rope[i] * (i+1)) # 로프가 들 수 있는 질량 * 병렬 연결 로프 개수

print(max(value))