

"""
요세푸스 순열 문제 원에서 사람들이 제거되는 순서

K번째 사람을 제거한다.

N명의 사람을 제거하기 위해 제거할 사람을 선택하는 행동을 총 N번 해야 한다.

경우마다 제거하는 사람을 찾기 위해 오른쪽으로 K번 움직여야 한다.

"""

N, K = map(int, input().split())

peo = [i for i in range(1, N+1)]

pt = 0

ans = []

for _ in range(N):
    pt += K -1
    pt %= len(peo)
    ans.append(peo.pop(pt))

print(f"<{', '.join(map(str, ans))}")