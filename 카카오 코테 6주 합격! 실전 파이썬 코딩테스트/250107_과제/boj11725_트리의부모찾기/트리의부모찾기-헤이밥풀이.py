import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
parents = [0] * (N + 1)

tree = { i: [] for i in range(1, N + 1)}

edges = [list(map(int, input().split())) for _ in range(N - 1)]

for edge in edges:
    s, e = edge
    tree[s].append(e)
    tree[e].append(s)

# 종료 조건 : 더 이상 방문할 곳이 없을 때
# 원래는 자기 자신이 None 일 때 이지만, 여기서는 None이 없으므로 변형 해준다.
# 재귀 호출: 트리 상에 연결된 곳으로 방문
# 데이터 통합 : 부모 정보를 담으면 된다.

def traverse(cur, parent):
    parents[cur] = parent

    for node in tree[cur]:
        if node == parent:
            continue

        traverse(node, cur)


traverse(1, 0)

print(*parents[2:], sep='\n')

