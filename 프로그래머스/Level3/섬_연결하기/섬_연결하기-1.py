def solution(n, costs):
    parent = [i for i in range(n + 1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        pa = find(a)
        pb = find(b)
        parent[pa] = pb

    def kruskal():
        costs.sort(key=lambda x: x[2])
        total = 0
        for a, b, cost in costs:
            if find(a) != find(b):
                union(a, b)
                total += cost
        return total
    return kruskal()


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))  # 4
