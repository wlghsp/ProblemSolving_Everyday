"""




출력: 
차량 번호가 작은 자동차부터 
청구할 주차요금 
"""


def parkinghour():
    pass


def matches(openTerm: str, closeTerm: str) -> bool: 
    for array in TOKENS:
        if array[0] == openTerm:
            return array[1] == closeTerm
    return False  

def solution(fees, records):
    answer = []
    cars = {}
    cars_num = []
    stack = []
    for r in records:
        a, b, c = r.split()
        cars[b] = 0

    for r in records:
        a, b, c = r.split()
        if c == "IN":
            stack.append([a, b, c])

        if b == stack[0][1] and c == "OUT":
            in_r = stack.pop()
            h, m = map(int, in_r[0].split(":"))
            in_totalm = h * 60 + m
            out_h, out_m = map(int, a.split(":"))
            out_totalm = out_h * 60 + out_m
            result = out_totalm - in_totalm
            cars[in_r[1]] += result

    print(cars)
    # 누적주차시간 계산

    # return answer


fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]
# [14600, 34400, 5000]


fees1 = [120, 0, 60, 591]
records1 = [
    "16:00 3961 IN",
    "16:00 0202 IN",
    "18:00 3961 OUT",
    "18:00 0202 OUT",
    "23:58 3961 IN",
]
# [0, 591]

fees2 = [1, 461, 1, 10]
records2 = [
    "16:00 3961 IN",
    "16:00 0202 IN",
    "18:00 3961 OUT",
    "18:00 0202 OUT",
    "23:58 3961 IN",
]
# [14841]


print(solution(fees, records))
