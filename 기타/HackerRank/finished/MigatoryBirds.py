# 관측된 새, 가장 많이 관측된 새 종류를 찾아내고 그 종류가 2개 이상이라면 id가 가장 낮은 새 종류의 id를
# 도출한다.

from collections import Counter


def migratoryBirds(arr):
    count_dict = Counter(arr)
    birdlist = list()
    for bird, freq in count_dict.items():
        if freq == max(list(count_dict.values())):
            birdlist.append(bird)
    return min(birdlist)


# arr = [1, 1, 2, 2, 3]
arr = [
    1,
    2,
    3,
    4,
    5,
    4,
    3,
    2,
]
print(migratoryBirds(arr))
