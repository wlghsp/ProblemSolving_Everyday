"""
큰 수 덧셈에 성공했다.
이번에는 큰 수 뺄셈에 도전하자.

입력
큰 수 a, b가 두 줄에 걸쳐 입력된다. (a, b는 100자리 이하)

출력
a-b의 결과를 출력한다.

입력 예시
11232412
3

출력 예시
11232409



"""

import sys
input = lambda : sys.stdin.readline().rstrip()


a = int(input())
b = int(input())

print(a-b)