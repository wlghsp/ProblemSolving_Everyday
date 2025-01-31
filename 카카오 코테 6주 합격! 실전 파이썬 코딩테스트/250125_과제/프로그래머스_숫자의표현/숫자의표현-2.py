def solution(n):
    answer = 0
    for i in range(1, n + 1):
        S = 0
        for j in range(i, n + 1):
            S += j

            if S == n:
                answer += 1
            elif S > n:
                break
    return answer
print(solution(15))

'''
O(N^2)이면 
1 - 10000
10000 * 10000 = 10^8 >= 4 * 10^7 으로 시간초과
but

위 코드에서는 S > N 일 때 조기종료하게 됨
j * (j + 1) / 2 > N 에서 종료
대략 j^2 = 2N
j = 루트 2N 
내부 반복문은 루트 2N 까지 연산 
외부반복문 N 이므로 연산횟수는 N * 루트 2N회 

* 시간복잡도 O(N * 루트 N)

'''