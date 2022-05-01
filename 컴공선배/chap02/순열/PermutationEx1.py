


from itertools import permutations


arr = [0,1,2,3]
k = []
for i in permutations(arr, 4):
    k.append(i)
print(len(k))