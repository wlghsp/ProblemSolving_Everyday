
from collections import defaultdict

def counter(w):
    int_dict = defaultdict(lambda : 0) # defaultdict(int)도 가능 int()함수는 0을 리턴

    for c in list(w):
        int_dict[c] += 1

    return int_dict


a = input()
b = input()


a_dict = counter(a)
b_dict = counter(b)

answer = "YES"
for k in a_dict.keys():
    if a_dict[k] != b_dict[k]:
        answer = "NO"

print(answer)
