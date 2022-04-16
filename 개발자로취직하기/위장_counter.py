
from collections import Counter
from functools import reduce

def solution(clothes):
        # 1 옷을 종류별로 구분하기
        counter = Counter([type for clothe, type in clothes])
        print(counter)
        # 2. 모든 종류의 count + 1을 누적해서 곱해준다.
        answer = reduce(lambda acc, cur: acc * (cur +1), counter.values(), 1)

        return answer -1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))