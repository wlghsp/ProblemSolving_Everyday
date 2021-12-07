"""
vega 선생님은 Miss 피자 가게의 단골 손님이다.
그는 이번 달부터 절약 생활을 시작했다.
그래서 그는 피자 가게에서 주문할 수 있는 피자 중 1 달러 당 열량이 최대가 되는 피자를 주문하고 싶어한다.
이러한 피자를 "최고의 피자"라고 부르기로 하자.

"최고의 피자"는 1종류가 아니다.
Miss 피자는 N 종류의 토핑에서 여러 종류를 자유롭게 선택하여, 도우 위에 올려 주문할 수있다.
같은 토핑을 2 개 이상 올릴 수 없다.
도우에 토핑을 하나도 하지 않은  피자도 주문할 수있다.
도우의 가격은 A 달러이며, 토핑의 가격은 모두 B 달러이다.

실제 피자 가격은 도우의 가격과 토핑 가격의 합계이다.
즉, 토핑을 k 종류 (0 ≦ k ≦ N) 한 피자의 가격은 A + k × B 원이다.
피자 전체의 칼로리는 도우 열량과 토핑 칼로리의 합계이다.
도우의 가격과 토핑의 가격, 그리고 도우와 각 토핑 열량 값이 주어 졌을 때, "최고의 피자"의 1 달러 당 열량의 수를 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에는 토핑 종류 수를 나타내는 하나의 정수 N (1 ≦ N ≦ 100)이 입력된다.
두 번째 줄에는 두 개의 정수 A, B (1 ≦ A ≦ 1000,1 ≦ B ≦ 1000)가 공백을 구분으로 입력된다. A는 도우의 가격, B는 토핑의 가격을 나타낸다.
세 번째 줄에는 도우의 칼로리를 나타내는 정수 C (1 ≦ C ≦ 10000)가 입력된다.
3 + i 행 (1 ≦ i ≦ N)는 i 번째의 토핑 칼로리 수를 나타내는 정수 Di (1 ≦ Di ≦ 10,000)가 입력된다.

출력s
"최고의 피자" 1 달러 당 열량의 수를 소수점 이하는 버리고 정수로 출력한다.

입력 예시   
3
12 2
200
50
300
100

출력 예시
37



"""

import sys
input = lambda: sys.stdin.readline().rstrip()

#1. 토핑 수 
n = int(input())

#2. a는 도우의 가격, b는 토핑의 가격
a, b = map(int, input().split()) 

#3. 도우의 칼로리
c = int(input()) 

#4. 토핑 칼로리
toppings = [] 
for _ in range(n):
    toppings.append(int(input()))

#5. 토핑칼로리 내림차순 정렬
toppings.sort(reverse=True)


#6. 
result = 0

kcal = 0 # 토핑 칼로리
cost = 0 # 토핑 가격

for topping in toppings:
    kcal += topping # 토핑 칼로리 더하기
    cost += b # 토핑가격 더하기 

    # 1 달러당 칼로리 = (총 칼로리: 토핑칼로리+토핑칼로리)/ (도우가격 + 토핑가격)
    cal = (c+kcal)//(a+cost) 
    
    #  
    if result < cal:
        result = cal

print(result)


