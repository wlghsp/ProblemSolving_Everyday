"""
9 0 0 18 0 0
9 0 1 18 0 0
12 14 52 12 15 30

9 0 0
8 59 59
0 0 38


"""
# 시간을 모두 초로 변환해서 그 차이를 구한 후 이를 시 분 초로 다시 변환

# import sys
# import datetime

# input = sys.stdin.readline


# def calc_workinghour(h):
#     start = int(h[0]) * 3600 + int(h[1]) * 60 + int(h[2])
#     end = int(h[3]) * 3600 + int(h[4]) * 60 + int(h[5])
#     gap_seconds = end - start
#     result = map(int, str(datetime.timedelta(seconds=gap_seconds)).split(":"))
#     return result


# a_hour = list(input().split())  # A 출퇴근 시간
# b_hour = list(input().split())  # B 출퇴근 시간
# c_hour = list(input().split())  # C 출퇴근 시간
# print(*calc_workinghour(a_hour))
# print(*calc_workinghour(b_hour))
# print(*calc_workinghour(c_hour))


# 계산해서 초로 바꿨고, 둘의 차를 구했고, datetime.timedelta(seconds=초)
# 초를 h:m:s로 변환한 후 결과값을 확인하며 문제를 풀어 시간이 많이 걸림.


# 코드개선
import sys

input = sys.stdin.readline


def calc_workinghour(h):
    start = h[0] * 3600 + h[1] * 60 + h[2]
    end = h[3] * 3600 + h[4] * 60 + h[5]
    time = end - start
    # 시, 분, 초 분할을 아래와 같이 계산함.
    h = time // 3600
    m = (time % 3600) // 60
    s = (time % 3600) % 60

    print(h, m, s)


a_hour = list(map(int, input().split()))  # A 출퇴근 시간
b_hour = list(map(int, input().split()))  # B 출퇴근 시간
c_hour = list(map(int, input().split()))  # C 출퇴근 시간
calc_workinghour(a_hour)
calc_workinghour(b_hour)
calc_workinghour(c_hour)


# for i in range(3):
#     fh, fm, fs, lh, lm, ls = map(int, input().split())
#     first = (fm * 60) + (fh * 3600) + fs
#     last = (lm * 60) + (lh * 3600) + ls
#     time = last - first
#     h = time // 3600
#     m = (time % 3600) // 60
#     s = (time % 3600) % 60
#     print("%d %d %d" % (h, m, s))
