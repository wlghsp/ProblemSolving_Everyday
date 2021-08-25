import sys

input = sys.stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# 신발끈 공식은 좌표평면 상에서 꼭짓점의 좌표를 알 때 다각형의 면적을 구할 수 있는 방법
# 신발끈 공식 x1, y1을 한번 더 나열하여 계산함.
a = x1 * y2 + x2 * y3 + x3 * y1
b = x2 * y1 + x3 * y2 + x1 * y3

result = abs(a - b) / 2.0

print("%.2f" % result)


# # A를 (0,0)으로 만들고 B, C 좌표에 A좌표를 뺀다.
# x2 -= x1
# y2 -= y1
# x3 -= x1
# y3 -= y1
# print(x2, y2, x3, y3)

# # B와 C의 좌표를 교차하여 곱해준 값들 끼리의 차를 2로 나눈
# # 값이 그 삼각형의 넓이
# res = abs((x2 * y3) - (y2 * x3)) / 2.0
# print("%.2f" % res)
