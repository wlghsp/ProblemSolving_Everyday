class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stk = []
        self._push_left(root)

    def next(self) -> int:
        node = self.stk.pop()
        self._push_left(node.right)
        return node.val

    def _push_left(self, node):
        while node:
            self.stk.append(node)
            node = node.left

    def hasNext(self) -> bool:
        return 0 < len(self.stk)


if __name__ == "__main__":
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
