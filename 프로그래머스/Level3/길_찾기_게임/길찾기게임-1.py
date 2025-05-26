import sys

sys.setrecursionlimit(10 ** 6)

class Node:
    def __init__(self, x: int, y: int, idx: int):
        self.x = x
        self.y = y
        self.idx = idx
        self.left = None
        self.right = None

def insert(parent, child):
    if parent.x > child.x:
        if parent.left is None:
            parent.left = child
        else:
            insert(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            insert(parent.right, child)

def build_tree(nodeinfo_with_idx):
    root = Node(*nodeinfo_with_idx[0])
    for i in range(1, len(nodeinfo_with_idx)):
        insert(root, Node(*nodeinfo_with_idx[i]))
    return root

def preorder(node, pre):
    if node is None:
        return
    pre.append(node.idx)
    preorder(node.left, pre)
    preorder(node.right, pre)

def postorder(node, post):
    if node is None:
        return
    postorder(node.left, post)
    postorder(node.right, post)
    post.append(node.idx)

def solution(nodeinfo):
    nodeinfo_with_idx = [[x, y, idx + 1] for idx, (x, y) in enumerate(nodeinfo)]
    nodeinfo_with_idx.sort(key=lambda x: (-x[1], x[0]))
    root = build_tree(nodeinfo_with_idx)
    pre = []
    preorder(root, pre)
    post = []
    postorder(root, post)
    return [pre, post]


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
# [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]