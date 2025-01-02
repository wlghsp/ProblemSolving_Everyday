import bisect

# 학생들의 시험 점수 리스트
array = [
    ('John', 20), ('Chloe', 50), ('Amy', 30), ('Ben', 45),
    ('Diana', 35), ('Evan', 55), ('Fiona', 25), ('George', 60),
    ('Hannah', 40), ('Ian', 10)
]

# 모듈 1: 배열을 정렬하기
array.sort(key=lambda x: x[1])  # 점수 기준으로 정렬

# 모듈 2: bisect 모듈 이용해서 특정 값의 위치 찾기
def find_rank(sorted_array, new_entry):
    scores = [score for name, score in sorted_array]
    position = bisect.bisect_left(scores, new_entry[1])  # 점수 위치 찾기
    rank = position + 1  # 등수는 1부터 시작
    return rank

# 새로운 값
new_entry = ('Sam', 57)

# 새로운 값의 등수 찾기
rank = find_rank(array, new_entry)

print(f"{new_entry[0]}의 등수: {rank}등")