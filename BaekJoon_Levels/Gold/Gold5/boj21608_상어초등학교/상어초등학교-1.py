"""
교실

"""
N = int(input())
class_room = [[0] * N for _ in range(N)]
students = [list(map(int, input().split())) for _ in range(N * N)]
