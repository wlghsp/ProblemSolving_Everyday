
N = int(input())

nodes = [list(input().split()) for _ in range(N)]

tree = {}

for node in nodes:
    root = node[0]
    left = node[1]
    right = node[2]
    tree[root] = [left, right]

def preorder(x):
    if x == '.':
        return
    print(x, end='')
    preorder(tree[x][0])
    preorder(tree[x][1])

def inorder(x):
    if x == '.':
        return
    inorder(tree[x][0])
    print(x, end='')
    inorder(tree[x][1])

def postorder(x):
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