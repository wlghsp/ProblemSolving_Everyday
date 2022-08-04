import sys
input = lambda : sys.stdin.readline().rstrip()


a_cards = list(map(int, input().split()))
b_cards = list(map(int, input().split()))

A_win, B_win, D, winner = 0, 0, 0, 'D'

for i in range(10):
    if a_cards[i] > b_cards[i]:
        A_win += 3
        winner = 'A'
    elif b_cards[i] > a_cards[i]:
        B_win += 3
        winner = 'B'
    else:
        A_win += 1
        B_win += 1

if A_win > B_win:
    print(A_win, B_win)
    print("A")
elif B_win > A_win:
    print(A_win, B_win)
    print("B")
else:
    print(A_win, B_win)
    print(winner)