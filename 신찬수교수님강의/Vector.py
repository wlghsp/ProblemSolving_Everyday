

class Vector:
    def __init__(self, *args):
        self._coords = list(args) # [x for x in args]

    def __str__(self):
        return str(self._coords)

    def __len__(self): # return its dimension
        return len(self._coords)

    def __getitem__(self, k): # return the value of kth dimension
        return self._coords[k]

    def __setitem__(self, k, val): # return the value of kth dimension
        self._coords[k] = val

v = Vector(1, 2, 3)
v[-1] = 9

for c in v:
    print(c, end=" ")

print()