
N = int(input())

tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(x):
    # 루트 -> 왼쪽 -> 오른쪽
    if x == '.':
        return
    print(x, end='')
    preorder(tree[x][0])
    preorder(tree[x][1])

def inorder(x):
    # 왼쪽 -> 루트 -> 오른쪽
    if x == '.':
        return
    inorder(tree[x][0])
    print(x, end='')
    inorder(tree[x][1])

def postorder(x):
    # 왼쪽 -> 오른쪽 -> 루트
    if x == '.':
        return
    postorder(tree[x][0])
    postorder(tree[x][1])
    print(x, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
