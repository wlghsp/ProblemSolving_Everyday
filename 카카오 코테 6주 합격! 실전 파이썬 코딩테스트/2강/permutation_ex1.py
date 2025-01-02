# 중복이 없고 순서 있는 4자리 비밀번호 생성하기
from itertools import permutations

my_arr = list(range(10))
print(my_arr)
result = list(permutations(my_arr, 4))

print(len(result)) # 10 * 9 * 8 * 7
print(result)

# 생각해보기: 경우의 수는? 만들어지는 비밀번호의 수는?
# 생각해보기: big O는?


