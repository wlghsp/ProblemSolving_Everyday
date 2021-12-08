'''



https://so-es-immer.tistory.com/entry/Codeup-%EC%BD%94%EB%93%9C%EC%97%85-2641-%EC%88%8F%EB%8B%A4%EB%A6%AC%EC%9D%98-%EA%B3%84%EB%8B%A8-%EC%98%A4%EB%A5%B4%EA%B8%B0-small
'''


import sys
input = lambda: sys.stdin.readline().rstrip()


def upStair(lev, prev, preprev):
    global cnt
    if lev > n:
        return
    if lev == n:
        cnt += 1
        return
    if prev != 3 and preprev != 3: # 전과 전전에서 3칸을 오르면 3칸을 오를 수 없다.
        upStair(lev + 3, 3, prev) # 3칸 오르는 경우
    upStair(lev + 1, 1, prev) # 1 칸 오르는 경우
    upStair(lev + 2, 2, prev) # 2 칸 오르는 경우

cnt = 0
n = int(input())
upStair(0,0,0)
print(cnt)
