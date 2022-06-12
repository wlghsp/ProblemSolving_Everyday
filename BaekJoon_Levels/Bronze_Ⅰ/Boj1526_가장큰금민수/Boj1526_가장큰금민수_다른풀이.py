import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

'''
1. 4와 7을 좋아함. 나머지 숫자 싫어
2. 금민수는 4와 7로만 이루어진 수
3. N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램 

이 문제 풀이 정말 다양함.
'''
ans = []
while True:
    flag = True
    for i in str(N):
        # 숫자는  4도 아니고, 7도 아니다. 둘다 아닐 때만 if문을 통과하여 flag가 False가 됨.
        if i != "4" and i != "7":
            flag = False
            N -= 1
            # 숫자가 줄어들면서 바로 for문의 N이 바뀜, 그리고 뒤에서부터 확인하므로 빠르게 값을 찾을 수 있다.
    if flag:
        print(N) # 찾았으면 바로 출력하고 break로 종료
        break


