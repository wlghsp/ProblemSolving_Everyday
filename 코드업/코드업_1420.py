import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
scores_dict = {}
scores = []
for _ in range(n):
    name, score = input().split()
    scores.append(int(score))
    scores_dict[score] = name # score를 key로 넣어 score로 학생 이름 검색이 가능하게 함. 
scores.sort(reverse=True) # 세 번째로 높은학생이니 내림차순 정렬
# 1. dict 키로 검색
print(scores_dict[str(scores[2])])


# sorted_dict = sorted(scores_dict.items(), key=operator.itemgetter(1))
# 인자값에 있는 key=operator.itemgetter(0)는 정렬하고자 하는 키 값을 0번째 인덱스 기준으로 하겠다는 것입니다.
# 0번째 인자는 Key입니다.
# 인자값에 있는 key=operator.itemgetter(1)는 정렬하고자 하는 키 값을 1번째 인덱스 기준으로 하겠다는 것입니다.
# 1번째 인자는 Value입니다.


# 2. for문을 활용하여 딕셔너리의 값으로 키를 찾음
# for key, value in scores_dict.items():
#     if value == scores[2]:
#         print(key)
