import sys


input = sys.stdin.readline


def RCP(play1, play2):  # 뒤에 수를 1 더하여 같으면 play1 승
    if play2 == 3:  # 3일 경우 1로 바꾸고 다른 수는 1 더해준다.
        play2 = 1
    else:
        play2 += 1

    if play1 == play2:  # 같으면 play1 승
        return 0  # set한 승리자의 숫자 위치
    else:  # 다르면 play2 승
        return 1  # set한 승리자의 숫자 위치


selections = list(map(int, input().split()))

fight = list(set(selections))  # set을 이용하여 중복을 없앤다.

if len(fight) == 2:
    print(selections.count(fight[RCP(fight[0], fight[1])]))
else:
    print(0)
