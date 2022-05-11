


from itertools import combinations

arr = [0,1,2,3]
k = []
for i in combinations(arr, 2):
    k.append(i)

print(len(k))