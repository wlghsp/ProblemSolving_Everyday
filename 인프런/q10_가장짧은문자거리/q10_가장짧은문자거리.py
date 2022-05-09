


s, t = input().split()

x = list(s)


p = 1000
answer = [0 for _ in range(len(s))]
# 오른쪽 방향 탐색, 문자 t에서 우측 방향의 거리를 구함
for i in range(len(x)):
    if x[i] == t:
        p = 0
        answer[i] = p # t를 만나면 그 자리 거리는 0이다
    else:
        p += 1 # t로부터의 거리를 증가시킴
        answer[i] = p # 거리를 담아줌


p = 1000
# 문자열의 끝에서부터 왼쪽 방향 탐색, 문자 t에서 좌측 방향의  거리를 구함.
for i in range(len(x)-1, -1, -1):
    if x[i] == t:
        p = 0; # t를 만나면 위와 달리 그냥 p 초기화, 0인데 그 값은 오른쪽 탐색에서 넣어줬음
    else:
        p += 1
        answer[i] = min(answer[i], p)


print(*answer)