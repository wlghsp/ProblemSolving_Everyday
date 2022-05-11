
N = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = []
for i in range(N):
    board.append(list(map(int, input().split())))

'''
행렬 가장자리 0으로 초기화 하는 법: 
첫 행과 끝 행에 [0]으로 초기화 한 행렬을 insert/append 하고, 
새 행렬 양 끝에 insert/append로 0 추가한다.
'''
board.insert(0, [0]*N)
board.append([0]*N)
for x in board:
    x.insert(0, 0)
    x.append(0)

'''
행렬에서 상하좌우 탐색하는 법: 
x,y좌표를 이동시켜주는 리스트인 dx[-1,0,1,0] dy[0,1,0,-1]를 만들고, 
[i+dx[k]][j+dy[k]]를 k 기준으로 4번 반복하면 상하좌우 탐색이 가능하다.
'''
answer = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if all(board[i][j] > board[i+dx[k]][j + dy[k]] for k in range(4)):
            answer += 1
'''
all(): 인자의 내용이 모두 참이어야 True 리턴. 
하나라도 False일 시 False 리턴. 
모두 참이어야 하는 경우를 찾을 때 하나하나 쓸 필요 없어서 유용할 듯.
'''

print(answer)

