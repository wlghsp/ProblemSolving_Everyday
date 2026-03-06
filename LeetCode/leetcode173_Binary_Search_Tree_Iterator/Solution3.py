class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        # node 부터 왼쪽 끝까지 stack 에 push
        while node:
            self.stack.append(node)
            node = node.left
        
    def next(self) -> int:
        node = self.stack.pop()
        # 오른쪽 자식이 있으면 - 거기서 다시 왼쪽 끝까지 push
        if node.right:
            self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


if __name__ == "__main__":
    #        7
    #       / \
    #      3  15
    #        /  \
    #       9   20
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    it = BSTIterator(root)
    print(it.next())     # 3
    print(it.next())     # 7
    print(it.hasNext())  # True
    print(it.next())     # 9
    print(it.hasNext())  # True
    print(it.next())     # 15
    print(it.hasNext())  # True
    print(it.next())     # 20
    print(it.hasNext())  # False
