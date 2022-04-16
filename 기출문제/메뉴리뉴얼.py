

from itertools import combinations

def solution(orders, course):
     answer = []

     # 1. 각 order 정렬
     for i in range(len(orders)):
         orders[i] = "".join(sorted(orders[i]))
         print(orders[i])


     # 2. course_len 마다 조합 생성
     for course_len in course:
         hash = {} # 딕셔너리 key와 value를 갖고 있음, 키 값을 통해 value를 얻음
         max = 0
         for order in orders:
             # 각 order를 기준으로 courseLength 만큼의 조합 만들기
             for comb in combinations(order, course_len):
                 key = "".join(comb)
                 new_value = hash.get(key, 0) + 1;
                 hash[key] = new_value
                 if max < new_value:
                     max = new_value
         # 3. 가장 많은 조합 저장
         if max > 1:
             for type in hash:
                 if max == hash[type]:
                     answer.append(type)
     answer.sort()
     return answer

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))