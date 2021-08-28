"""
5000 12000 8000

8000

2000 4000 3000

3000

입력 : 3명의 연봉
출력:  회사에 남는 사람의 연봉

연봉이 가장 높은 사람과 가장 낮은 사람 회사에서 나가야함. 

정렬하고 인덱스 1 값을 출력 

"""

import sys

input = lambda: sys.stdin.readline().rstrip()

salaryOfPeople = list(map(int, input().split()))

salaryOfPeople.sort()

print(salaryOfPeople[1])
