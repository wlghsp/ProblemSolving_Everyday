"""
5
5 10 10 15 20

1.00

0

divide by zero

후기
솔직히 다 나와 있어서 쉬운 문제였다. 
list(set())
"""
import sys
input = sys.stdin.readline


def get_prob(records):
    records_noduple = list(set(records))  # set을 이용하여 중복을 없앤다.
    # 기록 평균
    his_average = sum(records) / len(records)
    expect = 0
    # 기대값 도출
    for rec in records_noduple:
        expect += rec*(records.count(rec)/len(records))
    prob = his_average / expect
    return prob


n = int(input())
if n == 0:
    print("divide by zero")
else:
    records = list(map(int, input().split()))
    print("%.2f" % get_prob(records))
