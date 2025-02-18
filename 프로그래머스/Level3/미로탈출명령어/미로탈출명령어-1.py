"""
1. 격자의 바깥으로 나갈 수 없음
2. (x,y) -> (r,c) 거리 = 총 k
3. 같은 격자 방문 가능
4. 문자열 사전순으로 가장 빠른 경로 탈출

사람이 예시를 먼저 풀어보자

(x,y)에서 k번 이동 해서 (r,c)에 도달 하는 경우를 모두 담아서

정렬하여 첫번째 출력

4 ^ 2500
k = 2

ll, lr, lu, ld,
rr, rl, ru, rd,
uu, ul, ur, ud,
dd, dl, dr, du

경우의 수를 계산에 실수했다.
왜 실수? 어떻게 생각하는게 맞는지?

4 의 2500 승이라서 브루트포스 안됨

1. analogy  비슷한 문제로 비슷한 접근 찾아 오기
2. bottleneck 찾아 big o 개선 하기
3. 반복은 dp, 방문 하지 않아도 되는 경우 greedy

"""
def solution(n, m, x, y, r, c, k):
    answer = ''


    return answer


print(solution(3, 4, 2, 3, 3, 1, 5)) # "dllrl"